from fpdf import FPDF


def getWiFiConnections(device):
   return device.command("nmcli -f all dev wifi list")


def saveWiFiConnectionsToPDF(wifiConnections, filename="wifi_connections.pdf"):
      pdf = FPDF()
      pdf.add_page()
      pdf.set_font("Arial", size=12)
   
      for line in wifiConnections.splitlines():
         pdf.cell(0, 10, txt=line, ln=True)
   
      pdf.output(filename)
      print(f"WiFi connections saved to {filename}")