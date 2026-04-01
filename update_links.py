import os
import re

dir_path = r"c:\Users\Hari\Music\SEAKNOTS_FRONTPAGE"

mapping = {
    'Home': 'HomePage.html',
    'About Us': 'AboutPage.html',
    'ISO Tank Management': '#',
    'Tank Container Operators': 'ISOTankManagement.html',
    'Tank Container Agency': 'TankContainerAgency.html',
    'Tank Container Leasing': 'TankContainerLease.html',
    'Tank Container Depot': 'TankContainerDepot.html',
    'Other Products and Services': '#',
    'NVOCC Software': 'NvoccSoftwarePage.html',
    'Fleet Management System': 'FleetManagementSystem.html',
    'Freight Forwarding Solution': 'FreightForwardingSolution.html',
    'Container Tracking': 'ContainerTracking.html',
    'Container Depot': 'TankContainerDepot.html',
    'Leasing and Trading': 'TankContainerLease.html',
    'Blogs': 'BlogsPage.html',
    'NewsLetter': 'NewsLetterPage.html',
    'Contact Us': 'ContactUsPage.html',
    'Blog': 'BlogsPage.html',
    'ISO Tank Container Software': 'ISOTankManagement.html',
    'ISO Tank Management Solution': 'ISOTankManagement.html',
    'FLEET Management System': 'FleetManagementSystem.html',
    'Freight Forwarding Software': 'FreightForwardingSolution.html'
}

for filename in os.listdir(dir_path):
    if filename.endswith(".html"):
        filepath = os.path.join(dir_path, filename)
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original = content
            
            for text, link in mapping.items():
                pattern = re.compile(rf'(<a[^>]*href=")([^"]*)("[^>]*>\s*{re.escape(text)}\s*</a>)', re.IGNORECASE)
                content = pattern.sub(rf'\g<1>{link}\g<3>', content)
                
            if content != original:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Updated {filename}")
        except Exception as e:
            print(f"Error processing {filename}: {e}")
            
print("Done.")
