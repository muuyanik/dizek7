import struct
import wave
import os
import sys

def parse_sf2(filepath, out_dir):
    with open(filepath, 'rb') as f:
        data = f.read()

    print(f"Loaded SF2: {len(data)} bytes")
    
    # Locate 'smpl' subchunk inside sdta
    smpl_pos = data.find(b'smpl')
    if smpl_pos == -1:
        print("smpl chunk not found")
        return
    
    smpl_len = struct.unpack('<I', data[smpl_pos+4:smpl_pos+8])[0]
    smpl_data_offset = smpl_pos + 8
    print(f"smpl chunk found at {smpl_pos}, length: {smpl_len}")

    # Locate 'shdr' subchunk inside pdta
    shdr_pos = data.find(b'shdr')
    if shdr_pos == -1:
        print("shdr chunk not found")
        return

    shdr_len = struct.unpack('<I', data[shdr_pos+4:shdr_pos+8])[0]
    num_samples = shdr_len // 46
    print(f"shdr chunk found at {shdr_pos}, length: {shdr_len}, total samples: {num_samples}")

    os.makedirs(out_dir, exist_ok=True)
    sample_list = []

    pos = shdr_pos + 8
    for i in range(num_samples):
        chunk = data[pos:pos+46]
        pos += 46
        
        name = chunk[:20].decode('ascii', errors='ignore').strip('\x00').strip()
        start, end, loop_start, loop_end, sample_rate, pitch, pitch_corr, sample_link, sample_type = struct.unpack('<IIIIIBbhH', chunk[20:46])
        
        if end > start and sample_rate > 0 and len(name) > 0 and not name.startswith("EOS"):
            sample_list.append({
                'name': name,
                'start': start,
                'end': end,
                'sample_rate': sample_rate,
                'pitch': pitch
            })

    print(f"Valid samples found: {len(sample_list)}")
    
    # Filter for Baglama, Saz, Cura, Ud, Oud
    keywords = ['saz', 'bag', 'cura', 'ud', 'oud', 'tambur', 'kanun', 'ney']
    extracted = []
    
    for s in sample_list:
        name_lower = s['name'].lower()
        if any(kw in name_lower for kw in keywords):
            print(f"Matching sample: {s['name']} (Rate: {s['sample_rate']}, Pitch: {s['pitch']})")
            
            # Extract PCM bytes (each sample is 2 bytes 16-bit signed LE)
            byte_start = smpl_data_offset + (s['start'] * 2)
            byte_end = smpl_data_offset + (s['end'] * 2)
            
            if byte_end <= len(data):
                pcm_bytes = data[byte_start:byte_end]
                clean_name = "".join(c for c in s['name'] if c.isalnum() or c in ('-', '_')).rstrip()
                out_path = os.path.join(out_dir, f"{clean_name}.wav")
                
                with wave.open(out_path, 'wb') as wf:
                    wf.setnchannels(1)
                    wf.setsampwidth(2)
                    wf.setframerate(s['sample_rate'])
                    wf.writeframes(pcm_bytes)
                
                extracted.append((clean_name, out_path, s['sample_rate'], s['pitch']))

    print(f"Total extracted: {len(extracted)}")
    for name, path, rate, pitch in extracted:
        size = os.path.getsize(path)
        print(f" - {name}: {size} bytes at {path}")

if __name__ == '__main__':
    sf2_path = sys.argv[1] if len(sys.argv) > 1 else 'TURKISH-ARAB3.sf2'
    out_dir = sys.argv[2] if len(sys.argv) > 2 else 'samples'
    parse_sf2(sf2_path, out_dir)
