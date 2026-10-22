using System;
using System.Diagnostics;
using System.IO;

namespace DizekLauncher
{
    static class Program
    {
        [STAThread]
        static void Main()
        {
            try
            {
                string baseDir = AppDomain.CurrentDomain.BaseDirectory;
                string htmlPath = Path.Combine(baseDir, "dizek.html");
                
                // If dizek.html doesn't exist, check index.html
                if (!File.Exists(htmlPath))
                {
                    htmlPath = Path.Combine(baseDir, "index.html");
                }

                if (File.Exists(htmlPath))
                {
                    Process.Start(new ProcessStartInfo
                    {
                        FileName = htmlPath,
                        UseShellExecute = true
                    });
                }
                else
                {
                    System.Windows.Forms.MessageBox.Show(
                        "dizek.html dosyası bulunamadı:\n" + htmlPath,
                        "Dizek 7",
                        System.Windows.Forms.MessageBoxButtons.OK,
                        System.Windows.Forms.MessageBoxIcon.Warning
                    );
                }
            }
            catch (Exception ex)
            {
                System.Windows.Forms.MessageBox.Show(
                    "Başlatma hatası: " + ex.Message,
                    "Dizek 7",
                    System.Windows.Forms.MessageBoxButtons.OK,
                    System.Windows.Forms.MessageBoxIcon.Error
                );
            }
        }
    }
}
