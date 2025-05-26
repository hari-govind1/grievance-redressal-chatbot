import openai
import chromadb
import os

# Set your OpenAI API key
openai.api_key = ""
#os.environ["CHROMA_API_IMPL"] = "chromadb.api.local.Local" 
client = chromadb.PersistentClient(path="D:/New folder1")

# Initialize Chroma client
#client = chromadb.Client()
#client = chromadb.Client(path="D:/New folder1")

# Create a collection in Chroma
collection = client.get_or_create_collection('grievance_data')

# Your text chunks (ensure these are the chunks you have already split)
chunks = [
    #chunk_1 data
    """Administrative Department: Overview and Guidelines Description: The Administrative Department is a key support function within a college, responsible for managing the non-academic 
    operations of the institution. This department ensures smooth functioning by overseeing various administrative tasks such as student admissions, records management, fee collection, scheduling, and policy implementation.
      It is the primary point of contact for students regarding administrative matters and provides essential support to both students and staff. The Administrative Department is instrumental in maintaining the institution's 
      internal processes and ensuring compliance with regulations, creating a conducive environment for academic and extracurricular activities.Key Responsibilities of the Administrative Department:Student Admissions and Registration: The department manages the admissions process, from processing applications to confirming student enrollment. 
      It also oversees registration for courses and handles updates to student records.Fee Management: The Administrative Department is responsible for the collection of tuition fees, hostels fees, and other charges. It ensures timely fee payments and addresses any queries related to fee structures, discounts, and payment methods.
    Student Records and Documentation: The department maintains and updates student records, including academic performance, personal details, and attendance. It is also responsible for issuing documents such as transcripts, certificates, and ID cards.
    Timetable Coordination: This department works closely with the Academic Department to organize the academic timetable for students, faculty, and staff. It ensures that all schedules align and any conflicts are resolved promptly.""",
    #chunk-2 data
    """ Key Responsibilities of the Administrative Department: Staff Support and Payroll: The department handles the payroll of faculty and non-teaching staff, ensuring that salaries are processed on time. It also manages staff leave, attendance, and general welfare.
    Facility Management: Administrative staff oversee the allocation and maintenance of campus facilities, including classrooms, auditoriums, hostels, and sports facilities. They are responsible for the cleanliness and upkeep of these areas.Policy Implementation and Compliance: The department ensures that institutional policies
    , rules, and regulations are effectively implemented and followed. This includes compliance with accreditation standards and any legal or regulatory requirements.Communication and Notifications: The Administrative Department manages official communications, notices, and announcements related to student affairs, including events, 
    academic schedules, and policy changes.Grievance Redressal: This department plays a central role in handling student grievances related to administrative issues. It is responsible for resolving complaints and ensuring fair treatment of all students.Event Coordination: The department often assists in organizing college events, workshops, and conferences. 
    It handles logistics, resource allocation, and the coordination of necessary services.Guidelines for Students to Follow: Follow the Official Communication Channels: Stay updated by regularly checking emails, notice boards, and official notifications from the Administrative Department. Ensure that you follow the prescribed channels for any requests or grievances.
    Adhere to Administrative Deadlines: Timely submission of forms, fee payments, and document requests is essential. Missing deadlines for admission, registration, or fee payment can lead to complications or fines. """,
    #chunk-3 data
    """Guidelines for Students to Follow: Maintain Updated Personal Information: Keep your personal information, including contact details, address, and emergency contacts, up to date in the administrative records to avoid delays in communication or issues with document issuance.
    Clear Fees and Dues Promptly: Ensure that all fees, including tuition, hostel, library, and other charges, are paid on time. Keep receipts and documentation for all payments made and address any discrepancies promptly.
    Request Documentation Early: If you require transcripts, certificates, or other official documents, request them well in advance to avoid delays. Follow the procedure specified by the Administrative Department for document requests.
    Respect Administrative Policies: Understand and adhere to the institution’s policies, including those related to attendance, conduct, and code of ethics. Familiarity with these policies will help you navigate administrative processes smoothly.
    Use the Grievance Mechanism for Complaints: If you have any issues related to administrative matters, follow the formal grievance redressal procedure. Submit a clear and concise description of the problem and provide necessary supporting documentation.
    Provide Accurate Information: When submitting any forms or applications, ensure that all the information provided is correct. Mistakes or inaccuracies can lead to delays or complications in your request or record processing.""",
    #chunk_4 data
    """Guidelines for Students to Follow: Stay Informed About Timetables and Schedules: Keep track of academic and administrative timetables, exam schedules, and deadlines. This will help you plan your activities and avoid missing important events or requirements.
    Seek Assistance When Necessary: If you have trouble understanding any administrative processes or need help with paperwork, don’t hesitate to ask the staff. Administrative personnel are there to guide you and ensure that all processes run smoothly.
    Use Available Services Effectively: The Administrative Department provides services such as attendance records, fee payment assistance, and official correspondence. Make sure to use these services whenever necessary to ensure all your academic and personal requirements are met.
    Be Polite and Professional in Communications: When communicating with administrative staff, be respectful, clear, and professional. This will help in resolving your queries more effectively and maintain a positive relationship with the department.
    Follow Up on Pending Requests: If you have submitted a request or complaint and haven’t received a response in a reasonable time, follow up politely. Keep track of your requests and make sure they are processed within the prescribed timelines.
    Know Your Rights and Responsibilities: Be aware of your rights regarding administrative processes and the resources available to you. Understanding these will help you navigate the system more effectively.""",
    #chunk_5 data
    """ Guidelines for Students to Follow: Maintain Confidentiality of Sensitive Information: Any personal, academic, or financial details you share with the Administrative Department must be treated with confidentiality. Respect the privacy of your fellow students and staff in all matters.
    By adhering to these guidelines and actively engaging with the Administrative Department, students can ensure a smooth academic journey and avoid unnecessary delays or complications. Always stay proactive, organized, and respectful in all administrative dealings.
    GRIEVANCES: Delays in processing admission applications. Lack of transparency in the admission process. Issues with fee payment portal accessibility. Delay in issuing ID cards. Unclear refund policies for dropped courses.Errors in student records. Unresponsive administrative staff
    Lack of clarity regarding scholarship eligibility. Long wait times for document verification. Inconsistent processing of leave requests. Difficulty in obtaining official transcripts. Unavailability of important forms in time.
    Complicated procedure for changing courses.""",
    #chunk_6 data
    """GRIEVANCES:Delays in issuing hall tickets for exams. Problems with accessing online academic portals. Lack of communication about changes in academic deadlines. Inefficient handling of student complaints. Slow processing of hostel applications
    Lack of proper grievance redressal systems. Unclear or contradictory rules regarding attendance. Delays in issuing degree certificates Difficulty in getting accommodation for outstation students. Unprofessional behavior of administrative staff
    Poor management of student records. Lack of information on procedures for document submission. Confusion about payment deadlines and late fees. Delays in updating student status after course completion. Inefficient handling of student internships
    Unclear guidelines for applying for academic leave. Lack of support for international students regarding visa issues. Complicated procedure for hostel room allocation.""",
    #chunk_7 data
    """ GRIEVANCES: Difficulty in obtaining a bonafide certificate. Lack of transparency in the allocation of scholarships. Unclear policies for applying for revaluation of exams. Uncoordinated communication between departments
    Issues with student health insurance processing. Delay in processing student loan applications. Slow response to email queries regarding administrative matters. Difficulty in updating personal information in the system. Unavailability of online services for administrative tasks.
    Issues with updating academic records. Lack of transparency in the allocation of class schedules. Problems with the refund process for dropped courses. Confusing fee structure and payment options. Inaccurate or outdated contact information on the college website
    Delay in processing travel grant applications. Problems with accessing financial aid or bursary support. Confusion over course registration deadlines""",
    #chunk_8 data
    """GRIEVANCES: Delay in providing confirmation of admission. Issues with student attendance records not being updated correctly. Inconsistent processing of student loan deferrals. Lack of communication regarding hostel fees or charges
    Unclear policies for students with disabilities. Inadequate support for students facing administrative challenges. Difficulty in obtaining leave of absence from academic programs. Absence of a streamlined process for document authentication
    Problems with semester registration procedures. Lack of clarity regarding credit transfer policies. Slow processing of student complaints related to accommodation. Complicated process for changing personal details. Problems with exam center allocation
    Inefficient handling of foreign student visas. Difficulty in applying for summer internships or exchanges. Problems with issuing temporary student ID cards. Delay in providing student evaluation feedback.""",
    #chunk_9 data
    """GRIEVANCES:
Poor management of student orientation programs.
Lack of clarity on procedures for applying for semester breaks.
Unclear policies on withdrawing from courses.
Difficulty in changing or updating course preferences.
Inefficient processing of student travel requests for college-related events.
Lack of coordination between administration and academic departments.
Poor customer service from administrative help desks
Confusing documentation required for student visa renewals.
Lack of real-time updates on administrative procedures.
Absence of a centralized system for tracking administrative tasks.
Inconsistent implementation of administrative rules.
Inadequate information regarding college policies and procedures.
Unclear guidelines for fee reimbursement or waivers.
Delay in publishing final exam schedules.
Slow processing of student petitions or requests.
Problems with obtaining parking permits.
Inefficient management of alumni registration.
""",
    #chunk_10 
    """GRIEVANCES:
Problems with documentation of student achievements.
Unclear policies regarding transfers between colleges.
Issues with registration for extracurricular activities. 
Difficulty in submitting important documents due to poor infrastructure.
Unclear policies on student attendance during medical leave.
Confusion about deadlines for administrative applications.
Problems with the maintenance of student databases.
Delay in issuing leave certificates for students.
Issues with transferring grades to other institutions.
Confusion regarding deadlines for submitting thesis/dissertation proposals.
Slow processing of student feedback for improvement. 
Unclear communication about academic policy updates.
Difficulty in registering for club activities or events.
Unclear guidelines on late submission of assignments.
Problems with student housing and relocation.
Issues with managing student requests for special accommodations.
Lack of support for students seeking internship placement assistance.""",
    #chunk_11 data
    """ GRIEVANCES:
Inefficiency in managing student complaints related to academic and non-academic issues.
Lack of proper communication regarding class cancellations.
Delays in issuing course completion certificates.
Inefficiency in handling student feedback forms.
Complicated process for changing personal information on records.
Slow response to requests for character certificates.
Unclear rules for late fee payments.
Unclear or inconsistent examination rescheduling policies.
Unclear application process for internships or placements.
Lack of support for students seeking part-time jobs.
Unclear policies regarding hostel fee refunds.
Difficulty in obtaining official course completion letters.
Poor handling of student complaints regarding teaching quality.
Inefficiency in issuing bonafide certificates for various purposes.
Unclear rules for applying for educational leave.
Lack of information on how to apply for foreign exchange programs.""",
    #chunk_12 data
    """GRIEVANCES:
Problems with updating bank account details for fee payment.
Uncoordinated management of student health services.
Long waiting times for appointments with administrative officers.
Confusing registration procedures for extracurricular activities.
Inefficient handling of official transcript requests.
Delayed issuance of original certificates post-graduation.
Lack of clear communication regarding rules for conducting research projects.
Problems with accessing personal academic data on the portal.
Difficulty in getting approvals for academic conferences or competitions.
Unavailability of updated contact information for administrative departments.
Inconsistent communication about upcoming events or deadlines.
Lack of transparency in the process of assigning faculty advisors.
Delays in confirming examination results.
Lack of streamlined processes for issuing scholarship funds.
Problems with reserving campus facilities for student events.
Slow approval process for leave applications during exams."""
]

department_id = "Administrative department"

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

# Store the chunks and embeddings in Chroma DB
for i, chunk in enumerate(chunks):
    collection.add(
        documents=[chunk],
        embeddings=[embeddings[i]],
        metadatas=[
            {
                "chunk_id": i,
                "department_id": department_id
             }
            ],
        ids=[f"chunk_{i}"]
    )

print("Chunks and embeddings have been successfully stored in Chroma DB.")
