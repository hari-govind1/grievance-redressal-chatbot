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
    #chunk1 data
    """Academic Department: Overview and Guidelines Description:
The Academic Department is a core component of any college, responsible for managing and coordinating the academic affairs of students. It encompasses various functions related to curriculum planning, academic schedules, and faculty management. 
The department is the point of contact for students regarding their academic progression, course registration, and examination procedures. It plays a vital role in ensuring that students are equipped with the knowledge and skills necessary for their chosen field of study. 
The Academic Department also oversees the implementation of academic policies and works closely with other departments to ensure a seamless learning experience for all students.Key Responsibilities of the Academic Department:1. Course Management: The department organizes 
and offers a variety of courses as per the academic program, ensuring that the curriculum aligns with industry standards and academic excellence.2. Academic Counseling: Students can approach the department for guidance on course selection, academic difficulties, and career advice.
 Faculty members and academic counselors are available to provide academic support to help students excel in their studies.3. Examination and Evaluation: The department is responsible for conducting examinations, grading, and ensuring that academic standards are maintained. It also handles the issuance of results, 
 transcripts, and academic records. 4. Student Support Services: The department provides services such as academic advising, tutoring, and workshops aimed at enhancing students’ academic skills. It also helps resolve academic grievances related to exams, grades, and coursework.
 Research and Innovation: Many academic departments foster an environment of research and innovation. They encourage students to participate in research projects, submit papers, and engage in academic activities beyond the classroom.
6. Timetable Coordination: The Academic Department organizes the class schedules, exam timetables, and ensures proper allocation of resources (classrooms, equipment, etc.) for smooth academic operations.
 """,

    #chunk2 data
    """ Key Responsibilities of the Academic Department: 7. Request for Support Early: If you are struggling with coursework, grades, or personal issues affecting your academic performance, don’t wait for the problem to escalate. Approach the department early for support or accommodations.8. Stay Organized: Keep track of 
    important documents such as syllabi, assignment deadlines, and academic records. Use calendars, planners, or digital tools to manage your academic schedule effectively.9. Use Resources Wisely: Utilize the resources provided by the department, such as libraries, research materials, 
    study spaces, and online databases. These are essential tools for your academic success.10. Respect Departmental Rules: Follow the guidelines provided by the department regarding behavior, dress code, and interaction with faculty and fellow students. Respect for the academic environment fosters a positive and productive learning experience.
    GRIEVANCES: Delayed announcement of exam results.
    Unavailability of updated course materials.
    Lack of clarity in the syllabus provided.
    Inadequate response from faculty during consultation hours.
    Improper guidance for project work.
    Issues with online class connectivity.
    Inefficient scheduling of lectures and practicals.
    Frequent rescheduling or cancellation of classes.Lack of practical exposure during lab sessions.
    Unavailability of required lab equipment.
    Insufficient time for exam preparation.
    Errors in question papers. """,

    #chunk3 data
    """GRIEVANCES:Difficulty in accessing academic transcripts.
    Lack of opportunities for skill development.
    Improper evaluation of answer sheets.
    Unreasonable deadlines for assignments.
    Insufficient academic support for weaker students.
      Lack of elective courses as per interests.
Unavailability of required books in the library.
Non-cooperative behavior of faculty members.
Delays in issuing degree certificates.
Lack of industry-oriented curriculum.
Improper handling of student grievances.
Absence of timely feedback on assignments.
Lack of awareness about academic policies.""",

    #chunk4 data
    """GRIEVANCES: Insufficient faculty for certain subjects.
Poorly planned academic calendar.
Overlapping of classes with co-curricular activities.
Inefficient coordination between departments.
Lack of support for research initiatives.
Errors in student attendance records.Non-availability of faculty for doubt clarification.
Inadequate use of technology in teaching.
Absence of remedial classes for failed students.
Difficulty in registering for courses.
Limited availability of internships.
Lack of communication regarding timetable changes.
Ineffective handling of plagiarism cases.
Poor guidance for competitive exams.
Non-transparent grading system.Issues in group allocation for projects.
Unavailability of advanced courses.
Lack of faculty expertise in certain subjects.
Improper handling of student academic appeals.
Insufficient peer interaction opportunities.
Difficulty in accessing e-learning resources.""",

    #chunk5 data
    """ GRIEVANCES: Lack of preparation for viva or practical exams.
Unfair distribution of workload among students.
Lack of academic workshops or seminars.
Absence of academic mentorship programs.
Unclear guidelines for assignments and projects.
Lack of interaction between faculty and students.
Insufficient use of multimedia in teaching.
Unavailable faculty during office hours.
No proper orientation for new students.
Unstructured lecture content.
Lack of online resources for course material.
Slow resolution of academic queries.
Problems with accessing online exam portals.
No transparency in grading assignments.
Unfair peer evaluation during group projects.
Short notice about class changes.
Poor communication of academic requirements.
Lack of industry connections for career guidance.
Inadequate research facilities for students.""",

    #chunk6 data
    """ GRIEVANCES: Faculty not adhering to the prescribed syllabus.
Unclear or missing academic calendar updates.
Insufficient attention to students with special learning needs.
Lack of provision for make-up exams.
Frequent changes in faculty teaching subjects.
Absence of post-graduation guidance or counseling.
No provision for transferring academic credits.
Overly difficult exams with limited study material.
Poor quality of guest lectures or workshops.
Unclear expectations for final year projects.
Limited opportunities for academic collaborations.
Inconsistent assessment criteria.
Delays in providing course feedback to students.
Confusion over course prerequisites and requirements.
Inefficient grievance redressal system for academic issues.
Disorganization in exam hall allocation.""",

#CHunk7 data
"""GRIEVANCES : Lack of group study areas or academic lounges.
Unprofessional behavior by some faculty members.
Overcrowded classrooms affecting learning quality.
Poorly structured or inadequate field trips.
Limited choice of open electives.
Difficulty in scheduling remedial classes.
Lack of career-oriented courses in the curriculum.
Inconsistent attendance policies.
Failure to maintain proper records of academic performance.
Unclear or absent guidelines on thesis submission.
Disorganized handling of external examination systems.
Inadequate support for international students.
No recognition for extracurricular academic achievements.
Late release of final marksheets.
""",
#CHUNK8 data
""" GRIEVANCES: Poor student feedback mechanisms.
Lack of proper internship guidance.
Excessive focus on theoretical knowledge with little practical application.
Absence of counseling services for academic stress.
Difficulties in registering for electives or specializations.
Lack of clarity on course prerequisites.
Inconsistent teaching methods across faculty.
Insufficient focus on current industry trends.
Poor time management during lectures.
Delay in issuing grade sheets.
Unavailability of supplementary reading material.Poor faculty availability for research guidance.
Ineffective use of online learning platforms.
Inadequate training for teaching assistants.
Poor infrastructure for conducting research.""",

#chunk9 data
"""GRIEVANCES: Unclear deadlines for assignments and submissions.
Faculty not adhering to lecture schedules.
No opportunities for inter-departmental collaboration.
Lack of regular academic workshops and training.
Issues with the quality of research publications.
Difficulty in obtaining course credits for internships.
Unfair distribution of academic responsibilities among students.
Non-transparent evaluation criteria for practical exams.
Limited access to academic journals or research papers.
No focus on soft skills development in the curriculum.Lack of emphasis on project-based learning.
Delay in clearing backlogs or reappear exams.
Inadequate resources for online learning.
Disorganized thesis submission process.
Lack of clear communication on academic policies.
""",

#chunk 10 data
"""GRIEVANCES: Unresolved academic conflicts between faculty and students.
No clear guidelines on plagiarism policies.
Excessive theoretical workload in place of practical experience.
Difficulty in getting approval for academic leave.
No formal process for submitting academic complaints.
Non-availability of relevant software for courses.
Inconsistent feedback on assignments and exams.
Difficulty in transferring credits for foreign exchange students.
Lack of clarity on attendance exemptions or adjustments.
Unfair peer feedback during course evaluations.
Slow response to academic-related emails.
Non-availability of career development or counseling services.
Inefficient course registration system.
Poor coordination between academic departments.
""",

#chunk 11 data
"""GRIEVANCES: Lack of collaboration opportunities for students with faculty.
Insufficient practical exposure in professional courses.
Unclear guidelines for academic awards and honors.
No consideration for students with health issues during exams.
Disorganized internship or placement processes.
Poor quality of course materials (books, handouts).
Delays in the issuance of certificates or transcripts.
Inability to change courses after registration.
Difficulty in accessing digital course content.
Lack of professional development opportunities for students.Inefficiency in handling special academic requests like revaluation.
Lack of updated course outlines or syllabi.
Insufficient opportunities for student-faculty interaction.
No mentorship programs for academic development.
Faculty not providing timely feedback on assignments.
""",

#chunk12 data
"""GRIEVANCES: Unavailability of essential academic software or tools.
Lack of interdisciplinary learning opportunities.
Non-transparent grading system leading to confusion.
Unnecessary repetition of topics across courses.
Inefficient or delayed processing of academic appeals.
No clear guidelines for online exam proctoring.
No proactive communication about academic deadlines.
Unreasonable expectations for student presentations.
Lack of practical learning opportunities in theory-heavy courses.
Overloaded course schedules leading to burnout.No clear communication about research paper guidelines.
Inconsistent exam question formats leading to confusion.
Absence of workshops on research methodologies.
Unclear or inadequate academic policies for transfers or drops.
Inconsistent application of academic penalties for misconduct.
""",

#chunk13 data
"""GRIEVANCES: Lack of clarity on student rights and responsibilities.
Insufficient library hours during exam periods.
Excessive reliance on outdated textbooks.
No availability of tutoring services for difficult subjects.
Lack of support for creative or artistic subjects.
Issues with access to lab facilities outside of class hours.
Unnecessary competition among students instead of collaboration.
Insufficient exposure to real-world case studies or scenarios.
Inadequate facilities for group study sessions.Delay in resolving issues related to academic scholarships.
No formal recognition for academic achievements beyond grades.
Insufficient resources for students pursuing research projects.
Lack of timely updates on academic schedule changes.
Poor communication about academic eligibility criteria for events.
Inefficient process for applying for academic leaves.
Unfair distribution of research opportunities among students.""",

#chunk 14 data
"""GRIEVANCES: Lack of integration of soft skills development in academic courses.
No system for cross-course credit transfer.
Non-availability of extended library access during exam times.
Unorganized approach to online exams or assessments.
Lack of diversity in course offerings.
No opportunities for real-time interaction with industry experts.
Overemphasis on rote learning rather than critical thinking.
Inability to make course adjustments after the semester starts.Slow response from department offices regarding academic queries.
Lack of effective time management tools for students.
Poor integration of modern technology in the learning process.
No recognition of online learning achievements.
Lack of clarity on internship credit system.
Inefficiency in handling external examination results.
Problems with group project workload distribution.
"""
]

department_id = "Academic department"

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
