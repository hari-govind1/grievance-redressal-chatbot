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
    """Overview of the Placement Department.The Placement Department plays a crucial role in bridging the gap between the academic world and the professional industry. Its primary function is to assist students in securing internships, training programs, and full-time employment opportunities after graduation. The department works closely with companies, alumni, and other recruitment 
    partners to organize placement drives, career counseling sessions, workshops, and mock interviews, ensuring students are well-prepared for the job market.The department also helps students with career guidance, resume building, interview preparation, and job search strategies. The Placement Department aims to not only place students in relevant job roles but also provide them with 
    the necessary tools to develop professional skills that will serve them throughout their careersKey Responsibilities of the Placement Department: Industry Collaboration: Establish and maintain relationships with top companies, industries, and recruitment agencies to facilitate placement opportunities for students.Placement Drives: Organize campus recruitment drives, career fairs, 
    and recruitment events for final-year students.Internship Programs: Help students find internships that complement their academic learning and provide real-world experience.Career Counseling: Provide guidance on career choices, job market trends, and potential career paths based on students' skills and interests.Skill Development: Organize workshops, training sessions, and seminars 
    on job-ready skills, such as communication, negotiation, teamwork, and technical skills.""",
    #chunk-2 data
    """ Key Responsibilities of the Placement Department: Resume Building: Assist students in crafting professional resumes and cover letters tailored to specific job roles or industries.Mock Interviews and Group Discussions: Conduct mock interviews and group discussion sessions to help students prepare for real-time recruitment processes.Alumni Engagement: Foster connections between current 
    students and alumni to create mentorship opportunities and industry insights.Feedback Collection: Gather feedback from both students and recruiters to improve the placement process and refine future strategies.Guidelines for Students to Follow: Active Participation: Participate actively in placement-related activities like workshops, webinars, and mock interviews. These sessions are designed
    to enhance your skills and increase your chances of getting hired.Maintain Professionalism: Always act professionally during placement drives, interviews, and interactions with recruiters. This includes dressing appropriately, being punctual, and using professional language.Research Potential Employers: Before attending interviews or recruitment events, research the company, its culture, and 
    the roles being offered. This will help you ask relevant questions and demonstrate your interest during interviews.Update Your Resume Regularly: Ensure that your resume is always up-to-date with your academic achievements, extracurricular activities, internships, and any work experience. Tailor your resume for each position you apply to.Attend Pre-Placement Training: The Placement Department 
    organizes various workshops on resume building, communication skills, and interview techniques. Make sure to attend them to sharpen your skills.Be Flexible and Open-Minded: Be open to opportunities, even if they may not be in your preferred industry or role. An open mind and willingness to explore different paths can lead to rewarding career opportunities.""",
    #chunk-3 data
    """Guidelines for Students to Follow: Networking: Utilize the opportunity to connect with alumni, recruiters, and professionals from different industries during placement drives and career fairs. Networking can lead to valuable career insights and job referrals.Preparation for Aptitude and Technical Tests: Many companies conduct aptitude tests or technical assessments as part of their recruitment
    process. Be sure to practice and prepare for these tests to improve your chances.Follow Instructions: Always follow the instructions provided by the Placement Department regarding placement registration, interview schedules, and documentation. Missing deadlines or instructions can lead to missing out on placement opportunities.Post-Placement Etiquette: If you receive a job offer, ensure that you 
    inform the Placement Department and follow up with the company in a timely and professional manner. Similarly, if you decide to decline an offer, do so respectfully.Respect Confidentiality: Avoid sharing confidential information related to interviews or the recruitment process with others. Respect the privacy of both the company and fellow candidates.Timely Feedback: After attending an interview or 
    placement drive, provide feedback to the Placement Department. This helps the department improve future placement activities and assists in assessing your experience.Prepare for Group Discussions: Many companies evaluate candidates through group discussions (GDs). Practice GDs on various topics to develop your communication, listening, and teamwork skills.Keep a Positive Attitude: The placement process 
    can sometimes be competitive and stressful. Keep a positive attitude, and don’t get discouraged if things don't go as planned. Resilience and perseverance are important qualities in securing a job.Follow Up: If you have attended interviews but haven't received a response within the expected time frame, it's appropriate to follow up with the Placement Department or the company for updates.""",
    #chunk_4 data
    """Grievances
Limited number of companies visiting the campus for placements.
Lack of core company opportunities for specific branches.
Low salary packages offered by most recruiting companies.
No proper communication regarding placement drives and deadlines.
Insufficient training sessions for aptitude, GD, and interview skills.
Lack of internship opportunities through the Placement Cell.
Companies canceling interviews at the last minute.
No proper coordination between students and recruiters.
Biased selection process favoring certain students or departments.
Inadequate placement opportunities for students with low academic scores
No tie-ups with reputed multinational companies.
Placement process being lengthy and time-consuming.
No assistance provided for off-campus placements.""",
    #chunk_5 data
    """ GRIEVANCES: 
    Companies setting unrealistic eligibility criteria for students.
Lack of proper follow-up after initial placement rounds.
Limited availability of mock interview sessions.
No support for students looking for international job opportunities.
No guidance on preparing an effective resume and cover letter.
Placement cell not responding to student queries on time.
Companies recruiting only for sales and marketing roles, ignoring technical positions.
Placement policies not being transparent to students.
No proper tracking of student placement statistics.
No backup plan for students who don’t get placed in the first phase.
Limited opportunities for students from non-engineering backgrounds.
Lack of personality development and soft skills training.
No workshops on handling job offers, negotiations, and career planning.
Poor organization of placement drives, leading to chaos.
Limited career guidance for students unsure about job roles.
""",
    #chunk_6 data
    """GRIEVANCES:No clarity on rejection reasons after interview rounds.
No provision for reappearing in placement drives after an initial rejection.Unavailability of technical workshops to match industry standards.
No training for government job exams or public sector placements.
No placement opportunities for students interested in startups.
No support for students pursuing higher studies after graduation.
No provision for skill-based certifications to boost employability.
Companies withdrawing offers after initial selection.
Poorly maintained placement website with outdated job listings.
No exclusive placement opportunities for female students in certain industries.
Companies conducting multiple interview rounds without clear timelines.
Placement cell favoring students with internal references.
No financial support for students attending external job fairs.
No provision for industry expert talks and networking sessions.
Limited placement assistance for diploma and lateral entry students.
No preparation for students on handling workplace culture and ethics.""",
    #chunk_7 data
    """ GRIEVANCES: 
No clear process for grievance redressal related to placements.
Lack of job opportunities in diverse sectors beyond IT and finance.
No support for students aiming for research-based job roles.
Placement tests being outdated and irrelevant to current industry needs.
Companies imposing unfair bond periods or work conditions.
No clarity on pre-placement offers (PPOs) and internship conversions.
Placement cell failing to bring enough reputed companies to campus.
No structured mentoring program for students preparing for placements.
Unclear eligibility criteria for different companies and job roles.
No training on handling job rejections and career setbacks.
Placement registration process being complex and time-consuming.Students not informed about job descriptions before interviews.
No focus on entrepreneurship and startup support.
Companies withdrawing job offers without explanation.""",
#CHUNK8 data
""" GRIEVANCES: Students forced to accept low-paying jobs due to limited options.
No clarity on the selection process of companies visiting the campus.
Lack of industry-specific job opportunities for niche fields.
Placement cell favoring students with higher academic scores.
No assistance for students switching career domains.
Unfair shortlisting process where companies reject students without interviews.
No provision for rescheduling interviews for students with academic conflicts.
Placement team being unresponsive during peak placement season.
No direct connections with alumni for career guidance.
Limited placement options for students with backlogs.
Companies offering unpaid internships instead of full-time jobs.
No clarity on post-placement support for students.No training for online interviews and remote hiring processes.
Placement opportunities mainly restricted to metro cities.
Placement drives clashing with exam schedules.
""",

#chunk9 data
"""GRIEVANCES:No option for students to choose between different job offers.
Lack of company feedback to students after interview rejections.
Placement cell not negotiating for better salary packages.
No separate training for technical and non-technical roles.
Few companies offering work-from-home opportunities.
No special training for students aiming for government jobs.
Unavailability of proper placement reports from previous years.Placement team failing to respond to student concerns promptly.
No personalized career counseling sessions for students.
No workshops on freelancing or gig economy opportunities.
Limited networking opportunities with industry professionals.
Placement cell not updating students on industry trends.
Few job opportunities for students interested in R&D roles.No psychological support for students dealing with placement stress.
Companies setting unrealistic expectations for freshers.
Students not allowed to reapply to companies they were rejected from.
No separate placement assistance for postgraduate students.
""",

#chunk 10 data
"""GRIEVANCES:Few companies offering permanent job roles after internships.
Placement cell not maintaining a database of job openings for alumni.
No campus recruitment for emerging industries like AI and blockchain.
Students forced to attend placement drives for jobs they are not interested in.
No clarity on relocation assistance for students placed outside their hometowns.
Limited scope for creative and arts-related job placements.
Companies conducting mass hiring without clear job roles.
Placement cell failing to provide adequate training on coding rounds.
No access to real-world case studies or problem-solving challenges.
Limited diversity in job opportunities across various industries.No proper guidance for students interested in higher education over jobs.
Placement portal having outdated or incorrect job listings.
Companies canceling campus recruitment without prior notice.
Placement cell not following up with companies for pending results.
No clarity on job roles and responsibilities before interviews.
Few companies offering jobs with good work-life balance.
""",

#chunk 11 data
"""GRIEVANCES: Lack of industry partnerships for specialized career tracks.
No structured training for non-technical interview rounds.
Incomplete or incorrect company details shared with students.
No proper assistance for students aiming for government sector jobs.
Placement cell not supporting students with career gaps.
No job opportunities for students from non-traditional fields.
Poor coordination between different departments regarding placement schedules.
Companies reducing offered salary packages after selection.
Placement cell not helping students prepare for aptitude tests.
No placement support for students interested in defense jobs.
No transparency in company shortlisting process.
Limited access to placement preparation materials.
No reimbursement for students traveling for off-campus interviews.
No tracking of student placement status after graduation.Companies offering poor career growth opportunities.
No effort to invite global companies for international placements.
Placement cell failing to negotiate job terms with recruiters.
No training on how to handle workplace ethics and corporate culture.
""",

#chunk12 data
"""GRIEVANCES: Companies rejecting students for reasons not mentioned in eligibility criteria.
No provision for students with disabilities in placement drives.
No clarity on employment contract terms before signing.
Companies changing job locations after selection without informing students.
Placement cell not addressing discrimination concerns in recruitment.
No provision for students who want to switch fields post-graduation.
No database of alumni working in different industries for networking.
Limited or no companies offering research-based job roles.
Companies offering contractual jobs instead of permanent employment.
Placement cell not ensuring companies provide proper offer letters on time.
No guidance on handling multiple job offers effectively.
Lack of mentorship programs with senior industry professionals.
Placement cell focusing only on IT-based roles, ignoring other industries.
No internships available for first-year and second-year students.
No clarity on probation periods and post-hiring performance expectations.
Students getting placed in roles unrelated to their degree specialization.
""",

#chunk13 data
"""GRIEVANCES: No post-placement workshops on financial planning and salary management.
Limited assistance for students applying to foreign universities.
No workshops on personal branding and LinkedIn optimization.
Placement statistics being exaggerated or manipulated by the college.
No collaboration with professional certification providers for upskilling.
No special placement opportunities for women in STEM fields.
Placement cell not providing interview question banks for students.
No follow-up from placement cell to check job satisfaction of placed students.
No structured process for dealing with fake job offers or scams.
Companies delaying joining dates without proper communication.No dedicated placement support for students from economically weaker sections.
Companies imposing long and unfair bond periods on freshers.
Placement cell not helping students with visa sponsorship for international jobs.
No proper guidance for students wanting to switch from private to government jobs.
Poorly designed placement training sessions with outdated content.
No guidance on handling counteroffers from multiple recruiters.Placement cell not negotiating better relocation benefits for students.
Companies offering internships without the possibility of full-time conversion.
Placement process being rushed, leaving students unprepared.
No platform for students to share feedback about recruiters.""",

#chunk 14 data
"""GRIEVANCES: Companies rejecting students after final selection due to internal policies.
No mentorship programs with alumni working in top firms.
No effort to bring in companies offering remote or hybrid work roles.
No assistance for students wanting to pursue offbeat career paths.
Placement cell not considering student preferences in job allocation.
No job opportunities for students with prior work experience who want better roles.
No industry-specific resume-building workshops.
No initiative to conduct exclusive placement drives for women.
Companies ghosting students after promising further interview rounds.
No psychological counseling for students facing placement stress.

""",
#chunk15 data
"""GRIEVANCES: No coordination with academic faculty to ensure students are job-ready.
No special training for students struggling with English communication.
Placement cell prioritizing mass recruiters over quality jobs.
Students not given an option to defer their placement offers for higher studies.
No proper assessment of industry demands to align student skills.
Placement cell favoring companies that have prior ties with the institution.
No guidance on how to research a company before applying.
No initiative to track students who need placement reattempts.
Limited placement options for students from interdisciplinary courses.
No assistance for students looking for government fellowships.
"""

]

department_id = "Placement Department"

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
