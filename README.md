# Ports-Scanner-
A powerful tool to scan ports and find out if they are known to be vulnerable 
# **Ports-Scanner**  

A powerful and fast network scanning tool for scanning internet (WAN) and local network (LAN) targets. This tool detects open ports, services, and potential vulnerabilities.  

## **Features**  
✅ WAN Scan (Normal & High Scan)  
✅ LAN Scan (Detect Active Devices in a Local Network)  
✅ OS Detection (Windows/Linux)  
✅ Service and Version Detection  
✅ CVE-Based Vulnerability Lookup  
✅ Metasploit Exploit Search  

## **Installation**  

### **1. Clone the Repository**  
```sh
git clone https://github.com/yourusername/Ports-Scanner.git
cd Ports-Scanner
```

### **2. Install Dependencies**  
Make sure you have Python 3 installed, then run:  
```sh
pip install -r requirements.txt
```

### **3. Grant Storage Permissions (For Termux Users Only)**  
```sh
termux-setup-storage
```

### **4. Install External Dependencies (Required for Full Functionality)**  

#### **Linux / Termux:**  
```sh
pkg install nmap metasploit
```

#### **Debian/Ubuntu:**  
```sh
sudo apt update && sudo apt install nmap metasploit-framework exploitdb
```

## **Usage**  
Run the script using:  
```sh
python scanner.py
```

### **Main Menu Options:**  
1️⃣ **WAN Scan** - Scan internet-facing targets.  
2️⃣ **LAN Scan** - Scan local networks for active devices.  
3️⃣ **Install Metasploit Framework** (Optional)  
4️⃣ **Run Metasploit**  
5️⃣ **Exit**  

## **Example Output**  
```
ABU'S TOOLS
Developed by: Abubakar Bello
Contact: abubakarbello3914@gmail.com | +2347042725224
Special Thanks: Suryansh Gupta | syhsrthrug@gmail.com | +919839486431
============================================================

[+] Target OS: Linux
Scanning example.com (93.184.216.34) - Normal Scan...

[+] Open Port: 443
    ├─ Service: https
    ├─ Version: Apache/2.4.41
```

## **Contributing**  
Pull requests are welcome! Feel free to submit improvements, bug fixes, or new features.  

## **License**  
This project is open-source and licensed under the MIT License.
