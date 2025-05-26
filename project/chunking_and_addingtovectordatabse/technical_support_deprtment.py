import openai
import chromadb
import os

# Set your OpenAI API key
openai.api_key = ""
# Initialize Chroma client
client = chromadb.PersistentClient(path="D:/New folder1")

# Create a collection in Chroma
collection = client.get_collection('grievance_data')

# Your text chunks (ensure these are the chunks you have already split)
chunks = [
#chunk_1 data
    """IT/Technical Support: Overview and Guidelines Description: The IT/Technical Support department is responsible for maintaining and supporting the technological infrastructure of the college, including hardware, software, networking, and systems. It ensures that all technical resources, such as computers, internet services, and other digital tools, 
    function smoothly for students, faculty, and staff. The IT department helps address technical issues, provides troubleshooting, manages user accounts, and maintains the security of the college’s digital infrastructure. It plays a crucial role in ensuring that the technological needs of the academic environment are met, allowing for seamless learning, 
    communication, and administrative operations.Key Responsibilities of IT/Technical Support: Hardware and Software Maintenance: The IT department ensures that all hardware, including computers, printers, projectors, and other devices, are maintained and functioning properly. It also manages the installation, updating, and troubleshooting of software used 
    across the campus.Network Management: The department is responsible for the management of the college’s network infrastructure, including Wi-Fi, local area networks (LAN), and internet connectivity. It ensures that the network is stable, secure, and accessible to students and faculty.""",
    #chunk-2 data
    """ Key Responsibilities of IT/Technical Support: System Security: IT support ensures the safety and security of all devices, systems, and networks by implementing firewalls, anti-virus software, data encryption, and regular security updates. It also handles the protection of sensitive academic and personal data stored within college systems.User Support 
    and Help Desk: The IT support team provides assistance to students, faculty, and staff regarding technical issues. This includes troubleshooting problems with computers, software, network access, and other technology-related issues. The team responds to queries and provides step-by-step support to resolve problems.Account Management: IT support handles the 
    creation, maintenance, and troubleshooting of user accounts for students and staff. This includes email accounts, learning management system (LMS) access, and access to other institutional software and platforms.Installation and Setup of New Systems: When new hardware or software is introduced, the IT support team is responsible for installation and configuration. 
    This ensures that new systems are set up correctly and function as expected.Backup and Data Recovery: The department ensures that regular backups are taken for important data and systems, protecting against data loss. In the event of a system failure or data corruption, IT support manages data recovery procedures.Technical Training and Workshops: IT support may organize 
    training sessions or workshops for students and staff to enhance their technical skills, including tutorials on using the college’s learning management systems, productivity software, and other essential tools.""",
    #chunk-3 data
    """Key Responsibilities of IT/Technical Support: Software Licensing and Updates: IT support ensures that the college remains compliant with software licensing agreements and manages the updating of software to ensure that the latest versions are used.Troubleshooting and Issue Resolution: The IT department is responsible for resolving technical issues reported by students, 
    faculty, or staff. This may involve diagnosing hardware malfunctions, network problems, or software issues and taking appropriate action.Guidelines for Students to Follow:Report Technical Issues Promptly: If you experience technical problems, such as a malfunctioning computer, slow internet, or access issues with college systems, report the issue to the IT/Technical Support 
    department promptly. This helps in quick resolution and minimizes disruption.Provide Detailed Information: When reporting an issue, provide clear and detailed information about the problem, including the type of device you are using, the error message (if any), and the steps you have already taken to resolve the issue. This helps the support team in diagnosing the problem faster.
    Respect IT Resources: Treat all IT resources, including computers, printers, and networking equipment, with care. Avoid tampering with or altering hardware or software settings without permission, as this could cause malfunctions or security risks.Follow Security Guidelines: Be mindful of security protocols. Avoid downloading unverified software or clicking on suspicious links. 
    Use strong, unique passwords for your accounts and change them regularly. Be aware of phishing attempts and other cyber threats.""",
    #chunk_4 data
    """Guidelines for Students to Follow: Use College-Provided Software Only: Use the software provided by the college or approved by the IT department for academic and administrative purposes. Unauthorized or pirated software can compromise the security and stability of the systems.Keep Software Updated: Regularly update the software on your devices, including operating systems, 
    applications, and antivirus programs. Updates ensure that you have the latest features and security patches.Back Up Important Data: Regularly back up important academic work, files, and projects to external drives or cloud storage. This helps you prevent data loss due to unexpected system failures.Maintain Professional Conduct in the Computer Lab: If using college computer labs, 
    maintain a quiet and respectful environment. Avoid using the computers for non-academic purposes, and ensure that you follow the lab’s usage guidelines.Report Lost or Stolen Devices: If your college-issued device, such as a laptop or tablet, is lost or stolen, report it immediately to the IT department to protect sensitive information and prevent unauthorized access.Respect Privacy 
    and Confidentiality: Do not share your passwords, login details, or other personal information with others. Respect the privacy of your peers and faculty by not accessing or tampering with their devices or accounts.Follow Internet Usage Policies: Adhere to the college’s internet usage policies when accessing the network. Avoid excessive use of bandwidth for non-academic activities 
    and respect the time limitations for using the available computing resources.Clear Your Browser History and Temporary Files: If using college computers, make sure to log out of all accounts and clear your browser history, cookies, and temporary files when you finish using the system. This helps protect your privacy and security.""",
    #chunk_5 data
    """ Guidelines for Students to Follow:  Be Aware of College IT Guidelines: Familiarize yourself with the IT department’s policies regarding acceptable use of technology, including computer labs, internet access, and email services. Adhering to these guidelines ensures smooth functioning and avoids potential penalties.Attend IT Training Sessions: Participate in any IT workshops or training 
    sessions organized by the department. These sessions provide valuable information on how to use college software, troubleshoot common issues, and stay safe online.o Not Block or Disable Antivirus Software: Do not disable antivirus or firewall software installed on your devices. These tools are essential for protecting your device from viruses and cyber threats.Be Cautious with External Devices: 
    When connecting external devices, such as USB drives, ensure they are free from malware by scanning them with antivirus software before use. Avoid connecting personal devices to the college network without permission.Report Suspected Security Breaches: If you notice any suspicious activity, such as unusual login attempts or system errors, inform the IT department immediately so they can investigate 
    and take necessary action.Use College Email for Academic Purposes: Ensure that you use your college email account for academic communication. Do not share personal or non-academic information through official channels, as this can lead to privacy issues or security concerns.By following these guidelines, students can help the IT/Technical Support department maintain a smooth and secure technological environment, 
    ensuring that the systems and resources are available for academic use. The IT department is there to assist with technical issues, and maintaining a responsible approach to technology will help everyone get the most out of it.""",
    #chunk_6 data
    """GRIEVANCES:Slow response time for IT support requests.
Frequent Wi-Fi connectivity issues across campus.
Outdated computers in labs and faculty offices.
Software applications crashing frequently.
No proper guidance for using online learning platforms.
Difficulty in accessing university portals from home.
Delay in resolving student login issues.
Lack of technical support during weekends and holidays.
Limited access to licensed software for academic use.
No proper maintenance of projectors in classrooms.
Audio issues during online lectures or webinars.
Printers in labs not working properly.
Lack of training sessions for new IT tools.
Frequent power cuts affecting IT services.
No remote assistance for technical issues faced off-campus
Server downtime affecting student logins.
Lack of backup solutions for important data.
No dedicated helpline for urgent IT issues.""",
    #chunk_7 data
    """ GRIEVANCES: Poor integration between different academic software.
No clear escalation process for unresolved issues.
Slow internet speed in computer labs.
Campus websites and portals being outdated or non-functional.
No cloud storage options for student projects.
Difficulty in installing required software on personal laptops.
Delay in issuing university email credentials to new students.
No proper management of digital attendance systems.
Lack of security measures for protecting student data.
Technical staff being unresponsive to multiple complaints.
Smartboards in classrooms not functioning properly.
No self-service option for minor technical issues.
Unavailability of IT staff during crucial project submissions.
Frequent failures in online exam portals.
Limited storage space on university-provided accounts.
No live chat option for IT support.
Poor maintenance of coding and programming software.""",
#CHUNK8 data
""" GRIEVANCES: Issues with digital ID verification for university services.
No proper antivirus or cybersecurity measures on public computers.
Student accounts getting locked frequently without reason.
No quick reset option for forgotten passwords.
IT support team taking too long to update software.
Lack of proper documentation for troubleshooting common issues.
No systematic process for reporting hardware malfunctions.
Limited access to programming environments for computer science students.
Video conferencing tools not functioning well for hybrid classes.
No proper scheduling system for reserving IT labs.
No data recovery option for accidentally deleted files.
Issues with compatibility between different university software.
Limited number of computers available for use in the library.
No automatic notifications about system downtimes or maintenance.
No proper feedback system for IT service improvement.
No proper tracking system for IT support tickets.
Frequent glitches in the online student portal.
University Wi-Fi requiring frequent re-authentication.""",

#chunk9 data
"""GRIEVANCES:No dedicated IT support team for urgent classroom issues.
Slow performance of campus-provided email services.
Inconsistent access to cloud-based academic resources.
IT support ignoring follow-ups on unresolved issues.
Outdated operating systems on campus computers.
Frequent disconnections during online exams.
Difficulty in connecting personal devices to campus networks.
Lack of cybersecurity awareness training for students.
No proper maintenance of biometric attendance systems.
Difficulty in accessing online course materials.
Incompatibility of university software with personal devices.
Digital payment portals often failing during fee transactions.
No proper spam filtering for university email accounts.
Limited access to high-performance computing resources.
Lack of proper maintenance for CCTV surveillance systems.
Difficulty in integrating personal calendars with academic schedules.
No proper IT support for faculty conducting online classes.""",

#chunk 10 data
"""GRIEVANCES:Frequent bugs in online student registration systems.
Delay in issuing new or replacement ID cards.
No proper IT infrastructure for handling large-scale virtual events.
Problems with secure login authentication methods.
Lack of an automated system for IT inventory management.
No training on how to use LMS (Learning Management System) features.
Frequent crashes in the library’s digital catalog system.
No dedicated team to manage university social media accounts.
Poorly maintained website leading to broken links and outdated info.
Lack of access to digital textbooks through university resources.
No integration between library databases and student login systems.
No IT support for students using assistive technology.
Poor accessibility of online portals for students with disabilities.
No guidance on safely handling personal data on campus networks.
Limited IT support for students working on AI or big data projects.
Technical issues in scheduling and accessing virtual classrooms.""",

#chunk 11 data
"""GRIEVANCES: No single sign-on feature for multiple university services.
Lack of two-factor authentication for student portals.
No proper monitoring system for internet bandwidth allocation.
Difficulty in accessing previous semester’s digital coursework.
No proper IT maintenance schedule, leading to frequent breakdowns.
Student complaints about IT services taking weeks to be resolved.
Lack of a centralized knowledge base for troubleshooting.
Issues with exam proctoring software falsely flagging students.
Limited training on cybersecurity best practices for students.
Poor mobile app interface for accessing academic resources.
No proper digital record-keeping system for student complaints.
IT helpline not responding after office hours.
Lack of remote desktop access for students working on projects.
No proper coordination between academic departments and IT services.
No automated email alerts for scheduled system maintenance.""",

#chunk12 data
"""GRIEVANCES: University Wi-Fi coverage being weak in certain areas.No mobile authentication system for student logins.
Difficulty in retrieving lost or forgotten student IDs in IT systems.
No IT support for troubleshooting compatibility issues with academic software.
Poor coordination between IT support and academic departments.
Lack of proper data backup policies for student projects.
Inability to download required software due to licensing restrictions.
No IT support available for students during night study hours.
No online dashboard to track submitted IT complaints.
Difficulty in accessing university-provided VPN services.
No proper guidance on handling phishing or hacking attempts.
Faculty struggling with IT tools for digital assessments.
No easy process for students to request software installations in labs.
University-issued email accounts having very limited storage.
No self-service kiosk for resolving minor IT issues.""",

#chunk13 data
"""GRIEVANCES: Students unable to access university portals after graduation.
No IT training programs for non-technical students.
No dedicated forum for students to discuss IT-related queries.
Outdated student login portal with frequent login failures.
No centralized IT helpdesk number for all technical issues.
Campus printers running out of ink frequently without timely refilling.
Smart classrooms lacking proper IT maintenance.
No monitoring of cyberbullying or misuse of university networks.
Student accounts getting disabled without prior notice.
No structured process for requesting IT upgrades in labs.
Poor integration of third-party educational tools with university systems.
Outdated multimedia software in media and design labs.
Digital grading system often experiencing data loss.
IT staff refusing to help with personal device connectivity issues.""",

]

department_id = "Technical Support Department"

# Function to generate embeddings using OpenAI's model
def get_embeddings(text_chunks):
    embeddings = []
    for chunk in text_chunks:
        response = openai.Embedding.create(
            model="text-embedding-3-small",  # OpenAI model for embeddings
            input=chunk
        )
        embeddings.append(response['data'][0]['embedding'])
    return embeddings

# Generate embeddings for your chunks
embeddings = get_embeddings(chunks)

# Get the current number of documents in the collection (this will act as the sum)
current_docs = len(collection.get()['documents'])
sum = current_docs  # Set the sum to the current count of documents in the collection

# Store the chunks and embeddings in Chroma DB
for i, chunk in enumerate(chunks):
    # Add the sum as the document ID
    collection.add(
        documents=[chunk],
        embeddings=[embeddings[i]],
        metadatas=[{
            "chunk_id": i,
            "department_id": department_id
        }],
        ids=[f"chunk_{sum}"]  # Using the sum variable to generate unique document ID
    )
    
    # Increment the sum for the next document
    sum += 1

print("Chunks and embeddings have been successfully stored in Chroma DB.")
