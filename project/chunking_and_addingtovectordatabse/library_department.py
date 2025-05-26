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
    """Library Department: Overview and Guidelines.Description: The Library Department is an essential part of a college, providing students and faculty with access to a wide range of resources for academic and personal enrichment. It offers books, journals, electronic resources, research papers, 
    and other educational materials to support learning and research activities. The library serves as a hub for independent study, group discussions, and academic research, helping students to expand their knowledge beyond the classroom. The library is also responsible for maintaining the collection, 
    organizing resources, and ensuring easy access to materials for students.Key Responsibilities of the Library Department: 1.Resource Management: The library is responsible for acquiring, organizing, and maintaining books, journals, research papers, and other academic resources in both physical and digital formats. 
    It ensures that students have access to up-to-date and relevant materials for their courses and research.2.Cataloging and Retrieval: The department employs a cataloging system to classify and organize resources, making it easier for students and faculty to locate the materials they need. It also offers digital 
    databases and online resources that are accessible remotely.3. Research Assistance: Librarians assist students with finding research materials, databases, and citation resources. They also provide guidance on how to use library resources effectively for academic work.4. Reading and Study Facilities: The library 
    offers quiet and comfortable study areas where students can work independently or in groups. It provides designated spaces for reading, research, and collaborative work.5. Digital Resources and Access: The department ensures that students have access to electronic resources, including e-books, academic databases,
      online journals, and research papers. The library often provides access to software tools for academic research and writing.""",
    #chunk-2 data
    """ 6. Inter-Library Loans: In case the required material is not available in the library, the department facilitates inter-library loans, where students can borrow books or materials from other libraries in the network.7. Library Programs and Workshops: The library organizes programs such as book clubs, reading events,
     research workshops, and training sessions on library resources and research skills. 8. Maintaining Library Conduct: The library is responsible for ensuring that the library space is used respectfully. It enforces rules on noise levels, usage of computers, and borrowing materials.9. Book and Resource Recommendations: The 
     library regularly updates its collection based on faculty and student feedback, recommending new books or journals to enhance the library's resources.10. Borrowing and Return Management: The department manages the borrowing and returning process of books, journals, and other materials. It keeps track of overdue items and 
     ensures that resources are returned on time.Guidelines for Students to Follow: 1. Respect Library Timings: Adhere to the library's working hours, and make sure to complete any tasks, such as returning books, before closing time. Check the library schedule regularly, especially during exam periods, when extended hours might apply.
     2. Maintain Silence: The library is a quiet space for reading, studying, and research. Speak in low voices and ensure you maintain silence to avoid disturbing others.3. Handle Books and Resources with Care: Treat library materials with respect. Do not damage books, journals, or any other resources by marking, tearing, or scribbling on them. 
     Report any damaged items to the library staff.4. Return Borrowed Items on Time: Ensure you return books and other materials by the due date. Late returns can incur fines, and repeated delays in returning materials may lead to restricted borrowing privileges.""",
    #chunk-3 data
    """Guidelines for Students to Follow:5. Use Library Resources Responsibly: Use the library’s physical and digital resources responsibly. If you’re using a computer, make sure to follow the library’s guidelines regarding usage. Avoid downloading or printing unrelated personal content.6. Maintain a Clean Study Space: Clean up after using study spaces.
      Leave no trash behind and return any chairs or tables to their original position. Respect others who will use the space after you.7. Respect Library Staff and Fellow Students: Be courteous to library staff and fellow students. If you need assistance, ask staff members respectfully. If you notice any disruptions or issues, inform the staff calmly.
      8. Use the Catalogue and Digital Resources Efficiently: Make use of the library’s catalog and digital resources for research and studying. If you’re unfamiliar with these tools, ask a librarian for guidance on how to search for materials effectively.9. Avoid Food and Drinks in the Library: To maintain cleanliness and protect the library’s resources, 
      avoid bringing food and drinks into the library, unless otherwise specified.10. Limit Personal Conversations and Mobile Phone Use: Use your mobile phone outside of the library or in designated areas. Personal conversations should be kept to a minimum, as they can disrupt the study environment.11. Respect the Computer and Internet Usage Policy: If you are
     using the library’s computers or internet services, adhere to the library’s guidelines on internet usage. Do not engage in activities unrelated to your academic work.""",
    #chunk_4 data
    """Guidelines for Students to Follow:12. Keep Your Library Card Safe: Your library card is essential for borrowing books and accessing certain resources. Treat it with care and report any loss or theft immediately to the library staff.13. Be Aware of the Library’s Borrowing Limits: Understand the borrowing rules, including the number of items you can borrow 
    and the duration of the loan. Return books on time to avoid incurring late fees or losing borrowing privileges.14. Participate in Library Events: Engage in library-sponsored activities, such as reading events, book clubs, and workshops. These programs enhance your learning experience and contribute to the academic community.15. Notify the Library of Missing 
    or Lost Items: If you lose or misplace an item borrowed from the library, inform the staff immediately. They can help you locate it or guide you on how to resolve the issue.16. Avoid Misusing Library Resources: Refrain from using library resources for non-academic purposes. This includes improper use of computers, printers, and copying materials. Always follow 
    the ethical guidelines when using library resources for research. 17. Adhere to Copyright Laws: While using library resources, especially digital materials, follow copyright guidelines and fair use policies. Do not engage in illegal copying or distribution of copyrighted materials.18. Ask for Assistance When Needed: If you need help finding resources, navigating 
    the catalog, or using digital databases, don’t hesitate to ask a librarian. They are there to assist you and improve your research skills.19. Take Care of Online Access and Accounts: If you are accessing the library’s digital resources, ensure your login information is secure. Always log out of accounts after use and respect the guidelines for remote access.20. Report 
    Problems or Issues Promptly: If you encounter any technical issues with library resources, computers, or online systems, report them to the library staff so they can be resolved quickly and efficiently.""",
    #chunk_5 data
    """ GRIEVANCES: GRIEVANCES:
Insufficient number of copies for popular books
Limited library hours
Difficulty in finding required books
Outdated books and reference materials
Books missing from shelves without proper records
Long waiting time for book issuance
Lack of proper seating arrangements
Noisy environment affecting study concentration
Poor internet connectivity in the library
Limited access to digital resources and e-books
Damaged or torn books in circulation
Strict return deadlines leading to fines
High penalty charges for late book returns
Lack of subject-specific journals and periodicals
Unavailability of previous years’ question papers
Library staff being uncooperative or rude
Limited access to certain book sections
Poor air circulation making the library uncomfortable
Insufficient charging points for laptops and mobiles
Technical issues with the library management system
Non-functional barcode scanners causing delays
Slow response to book request applications
Lack of proper book return/dropbox facility
Restricted access to online library portals
Lack of clear library usage guidelines
No proper arrangement for group study discussions""",
    #chunk_6 data
    """GRIEVANCES:Lack of security for personal belongings
Frequent misplacement of books in wrong sections
Limited number of book renewals allowed
Computers in library being outdated or malfunctioning
Printing and photocopy services being too expensive
Non-availability of library staff during peak hours
Unhygienic condition of study desks and chairs
Excessive restrictions on bringing personal books
Limited working hours during examination periods
Lack of proper ventilation making the library stuffy
Unauthorized people occupying study spaces
No facility for borrowing reference-only books
Inadequate lighting in certain sections of the library
Lack of multilingual books for diverse students
Lack of online catalog for book availability checking
Damaged furniture making seating uncomfortable
No reminder system for due dates of books
Students not following silent study rules
No proper arrangement for return of inter-library books
Poor enforcement of book borrowing limits
Limited access to newspapers and magazines
Lack of a digital book request system
Insufficient budget allocated for library improvement
Lack of a suggestion/complaint box for student feedback
Delay in updating newly arrived books in the catalog
Books being issued to faculty before students get access
Lack of sufficient seating space during peak hours""",
    #chunk_7 data
    """ GRIEVANCES: Library website being outdated or non-functional
No proper system for reserving study spaces
Limited borrowing privileges for certain student categories
Library staff being unresponsive to queries
Lack of study-friendly environment due to poor acoustics
Unavailability of required software on library computers
Books often being misplaced or arranged incorrectly
No proper tracking system for issued books
Delays in restocking books returned by students
Insufficient lockers for students to store belongings
No digital access to research papers and thesis
Limited number of copies for high-demand reference books
Lack of flexible membership options for students
No mobile app for easy access to library services
Poor signage leading to confusion in book sections
No real-time tracking of book availability
Insufficient funding for purchasing new books
Some students reserving multiple seats unfairly
No proper arrangement for borrowed books to be extended online
Lack of advanced search filters on the digital catalog
Restricted access to books from other departments
Difficulty in accessing archives or historical documents
Lack of a proper lost-and-found system for misplaced items
No dedicated space for students working on research projects""",
#CHUNK8 data
""" GRIEVANCES: Some students damaging books intentionally without consequences
No online grievance redressal system for library issues
Library policies being too rigid and outdated
Long queues for issuing or returning books
Limited access to library resources for part-time students
Poor maintenance of digital screens or search kiosks
Lack of subscription to reputed academic databases
Library furniture being too old and uncomfortable
Lack of digitized versions of textbooks for easy access
No personalized recommendation system for books
Poor maintenance of air conditioning or heating
Restricted access to external research journals
Wi-Fi speed being too slow for research purposes
Library materials being lost frequently due to theft
No separate reading rooms for research scholars
Poor communication about book donation policies
No system to request out-of-stock books in advance
Limited printing and photocopying facilities
Absence of multimedia resources for interactive learning
No clear communication about library rules and penalties
Some books being permanently marked as "not for lending"
Limited access to international publications
Lack of study cubicles for students preferring isolated study
Lack of proper lighting in reading sections
Unavailability of book reservation system for students
Some books missing pages or having torn content
Lack of digital newspapers and magazines
Library assistants not helping students properly""",

#chunk9 data
"""GRIEVANCES:Frequent power cuts affecting reading and research
Noisy air conditioners or fans causing distractions
Insufficient tables for group study discussions
Books not arranged according to subject classification
No proper system to request inter-library loans
Damaged barcode stickers leading to scanning issues
Delay in restocking returned books on shelves
Library rules being inconsistent or not well enforced
Lack of guidance for first-year students on library usage
Books kept in inaccessible or locked shelves
Frequent server downtime of digital library services
No specific area for students to use personal laptops
No clear instructions on using the catalog search system
No proper security to prevent book theft
Lack of separate sections for competitive exam materials
Poor organization of books leading to difficulty in finding them
No lending option for research papers or journals
Students misusing reading areas for non-academic purposes
Limited access to previous research projects and dissertations
No access to international university databases
Expired book editions still being issued to students
No proper system for updating students about new arrivals
Lack of adequate digital scanning facilities
Some students hoarding books and not returning them on time
Lack of noise control leading to a disruptive atmosphere
No dedicated space for online learning within the library
Limited number of chairs compared to student demand
""",

#chunk 10 data
"""GRIEVANCES:Some books having missing index pages, making searching difficult
Lack of integration between library systems and academic portals
No backup power system for uninterrupted library use
No access to audiobooks or visually impaired-friendly materials
Some students violating book return policies without penalties
Lack of proper ventilation leading to stuffy conditions
Photocopy services being too expensive for students
No access to rare books or special collections
Delays in approving requests for book purchases
Library staff showing favoritism in book lending
Poor maintenance of bookbinding, leading to loose pages
No system to track the reading history of students
No penalty for students who damage library resources
Insufficient budget allocation for library development
Limited access to online research tools and citation software
Some students reserving books but not collecting them on time
No digital borrowing options for e-books or PDFs
No training sessions for students on how to use library resources effectively
No system to notify students when a requested book becomes available
Library staff not being available for assistance during peak hours
Difficulty in accessing thesis and dissertations from past students
Lack of foreign language books for language courses
Frequent system failures in the library management software
No clear differentiation between reference and borrowable books
Lack of proper maintenance of rare or antique books
No initiative to expand digital book collections
Limited accessibility for students with disabilities
No proper cataloging of new arrivals, leading to confusion
No 24/7 study area for students during exams
""",

#chunk 11 data
"""GRIEVANCES: No self-service kiosks for faster book borrowing
Delay in updating students’ borrowing status in the system
Lack of access to industry-specific magazines and journals
Insufficient space for students to sit comfortably
Library being closed for long durations on public holidays
Difficulty in finding books based on subject categories
No way to track lost or stolen books effectively
Library computers having outdated operating systems
Limited guidance on how to use digital resources effectively
No proper feedback system for library improvements
Difficulty in accessing research papers from external sources
No mobile-friendly interface for library services
No extended borrowing options for final-year students
Limited reference material for project and thesis work
Students not being informed about library rule changes
No live chat or email support for library queries
Unavailability of study lamps for night-time reading
Lack of policy enforcement for returning borrowed books on time
""",

#chunk12 data
"""GRIEVANCES: No proper coordination between different departmental libraries
Some books having missing barcodes, leading to scanning issues
No proper guidelines for donating books to the library
Limited access to university collaboration libraries
Absence of faculty recommendations for book purchases
Lack of training programs for library staff
No separate reading rooms for faculty members
Some important books being kept in restricted-access sections
No digital archive for students to submit their research papers
Lack of book exchange programs between universities
Limited borrowing privileges for students compared to faculty
No real-time status updates on books being returned
Lack of proper hygiene maintenance in library premises
No proper structure for extending book borrowing deadlines
No initiative to replace lost books with newer editions
No security system to prevent unauthorized access to library resources
Library policies being too rigid, affecting student convenience
No clear policy on using personal laptops inside the library
No grievance redressal mechanism specifically for library issues
Lack of proper labeling on book sections, making searches difficult
No suggestion box for students to recommend books
"""

]

department_id = "Library Department"

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