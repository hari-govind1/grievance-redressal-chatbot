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
    """Hostel Management Department: Overview and Guidelines: Description: The Hostel Management Department is responsible for managing and overseeing the residential facilities for students within the college. This department ensures that students residing in hostels have a comfortable and secure environment for their stay. 
    It handles all aspects of hostel life, including room assignments, food services, cleanliness, safety, and maintenance. The Hostel Management Department also enforces the rules and regulations that maintain order within the hostel and ensures that students have the support they need while living on campus.Hostel Department is responsible 
    for managing and overseeing the residential facilities for students within the college. This department ensures that students residing in hostels have a comfortable and secure environment for their stay. It handles all aspects of hostel life, including room assignments, food services, cleanliness, safety, and maintenance. 
    The Hostel Management Department also enforces the rules and regulations that maintain order within the hostel and ensures that students have the support they need while living on campus.Key Responsibilities of the Hostel Management Department: Room Allocation and Maintenance: The department oversees room assignments for students, 
    ensuring fair and transparent allocation.Allocation and Maintenance: The department oversees room assignments for students, ensuring fair and transparent allocation. It is also responsible for the maintenance and repair of hostel rooms, ensuring that they are in good condition for students.Food Services: The department manages the 
    mess or canteen services, including meal planning, preparation, and serving. It works to ensure that nutritious and hygienic food is provided to students on time.""",
    #chunk-2 data
    """ Key Responsibilities of the Hostel Management Department: Cleanliness and Hygiene: The Hostel Management Department ensures that hostels are regularly cleaned and maintained, including common areas such as bathrooms, corridors, lounges, and dining rooms.Security and Safety: Ensuring the safety and security of students is a key 
    responsibility of the department. This includes providing 24/7 security personnel, installing safety measures like CCTV cameras, and addressing any security concerns raised by students.Facilities Management: The department ensures that hostel facilities, including Wi-Fi, electricity, water supply, and common recreational areas, are 
    maintained and functioning properly.Grievance Redressal: The department serves as a point of contact for hostel-related grievances. It addresses issues such as room conditions, food quality, noise, safety, and any other concerns students might have regarding hostel life.Visitor Management: The department enforces policies regarding visitor access
    to the hostel and ensures that students' visitors follow the established protocols.Hostel Regulations and Compliance: The department is responsible for ensuring that students follow hostel rules and regulations, such as curfew timings, visitor policies, and behavior standards.Event and Community Building Activities: Many hostels organize social and 
    recreational activities for students to foster a sense of community. The department may also help coordinate events such as cultural nights, sports tournaments, and hostel gatherings.Emergency Support: In case of emergencies such as medical issues, accidents, or unforeseen circumstances, the department provides support, guidance, and resources to ensure students’ well-being.
    Guidelines for Students to Follow: Respect Hostel Rules and Regulations: Adhere to the rules set by the hostel management, including curfew timings, behavior expectations, and guest policies. Violation of rules can lead to penalties or even eviction.""",
    #chunk-3 data
    """Guidelines for Students to Follow: Maintain Cleanliness in Your Room: It is your responsibility to keep your room clean and tidy. Proper waste disposal, organizing your belongings, and maintaining hygiene should be prioritized for a healthy living environment.Use Hostel Facilities Responsibly: Be mindful of the resources provided in the hostel, such as electricity, water,
    and Wi-Fi. Avoid wasting these resources and report any malfunctions or issues to the hostel management immediately.Follow Dining Rules: Follow the rules regarding meals in the hostel mess, including timing, seating arrangements, and cleanliness. Always maintain decorum while using the dining facilities and avoid food wastage.Respect Quiet Hours: Be considerate of your fellow 
    hostel mates and respect quiet hours, especially during late-night and early-morning periods. Keep noise levels to a minimum in common areas and rooms.Report Maintenance Issues Promptly: If you notice any maintenance issues, such as broken furniture, leaks, or electrical problems, report them immediately to the hostel management so they can be addressed quickly.Keep Emergency 
    Contacts Handy: Familiarize yourself with the hostel’s emergency procedures and contact numbers for security, medical assistance, or other emergencies. In case of urgent situations, do not hesitate to seek help.Keep Emergency Contacts Handy: Familiarize yourself with the hostel’s emergency procedures and contact numbers for security, medical assistance, or other emergencies. 
    In case of urgent situations, do not hesitate to seek help.Be Mindful of Visitors: Follow the hostel’s visitor policies. Visitors should be registered at the front desk and should not stay beyond the allowed visiting hours. Ensure that visitors adhere to hostel rules as well.Use Common Areas Considerately: The common areas, such as lounges and study rooms, are shared spaces. 
    Ensure you use them respectfully, leaving them clean after use. Avoid monopolizing spaces for extended periods, especially when others are waiting.""",
    #chunk_4 data
    """Guidelines for Students to Follow: Be Mindful of Visitors: Follow the hostel’s visitor policies. Visitors should be registered at the front desk and should not stay beyond the allowed visiting hours. Ensure that visitors adhere to hostel rules as well.Use Common Areas Considerately: The common areas, such as lounges and study rooms, are shared spaces. Ensure you use them
    respectfully, leaving them clean after use. Avoid monopolizing spaces for extended periods, especially when others are waiting.Respect Roommates' Privacy and Preferences: If you share a room with a roommate, respect their privacy and personal space. Communicate openly to avoid misunderstandings and ensure a peaceful living environment.Stay Calm During Conflicts: In case of any
    issues or conflicts with roommates or neighbors, address them calmly and respectfully. If the issue persists, approach the hostel management for assistance in resolving the situation.Take Care of Your Belongings: Keep your personal belongings secure at all times. While the hostel management may provide basic safety, you are ultimately responsible for your valuables. Use lockers 
    or safes where available.Comply with Check-in and Check-out Procedures: Follow the procedures for checking in and checking out of the hostel. Ensure all necessary documentation is completed and submit any necessary forms or fees on time.Help Maintain Hostel Security: Always lock your door when you leave your room. Be vigilant about any suspicious activity and report it to the hostel 
    authorities or security personnel immediately.Participate in Hostel Activities: Engage in events and activities organized by the hostel. These activities help foster a sense of community and improve your overall living experience.Notify Management of Health Issues: If you are feeling unwell, inform the hostel management or the medical officer as soon as possible. This ensures that 
    proper care can be provided and prevents the spread of illness to others.Respect the Surrounding Environment: Maintain the cleanliness of the hostel’s surroundings. Dispose of trash properly, avoid littering, and be mindful of the environmental impact of your actions.""",
    #chunk_5 data
    """ Guidelines for Students to Follow: Cooperate with Staff: Treat hostel staff with respect and cooperation. They are there to ensure your safety and comfort, and a positive relationship with them will help resolve issues quickly.Respect Quiet and Study Areas: If your hostel has designated study areas, respect their purpose. Ensure that these spaces remain quiet and conducive to study, 
    especially during exam periods.Be Aware of Hostel Policies for Holidays and Vacations: Before going on break or vacation, ensure you are aware of the hostel policies regarding holiday leaves, room bookings, and check-out procedures to avoid any last-minute confusion.By following these guidelines, students can ensure a harmonious living environment in the hostel, fostering a sense of community
    while maintaining individual comfort and safety. Active communication with hostel management and adherence to hostel rules contribute to a better quality of life for all residents.GRIEVANCES: Lack of availability of hostel rooms.
Delay in room allotment process.
Poor quality of food served in the hostel.
Unhygienic living conditions.
No proper cleaning schedule for hostel rooms.
Inadequate lighting in hostel rooms.
No proper ventilation in rooms or common areas.""",
    #chunk_6 data
    """GRIEVANCES:Unavailability of clean drinking water.
Unmaintained or broken furniture in rooms.
Insufficient hot water supply.
Inconsistent electricity supply or frequent power cuts.
Lack of air conditioning or cooling systems in hot weather.
Poor internet connectivity in the hostel.
No proper waste disposal system.
No privacy in hostel bathrooms or showers.
Noise disturbances from nearby rooms or common areas.
Limited access to kitchen or cooking facilities.
Overcrowded hostel rooms.
Unhygienic toilets or bathrooms.
No provisions for vegetarian or special dietary needs.
Delayed or inadequate maintenance of hostel infrastructure.""",
    #chunk_7 data
    """ GRIEVANCES: Inadequate security measures in the hostel.
Lack of fire safety measures or equipment.
Limited recreational or common areas.
Poor behavior of fellow hostel mates or room sharing conflicts.
Poor behavior of fellow hostel mates or room sharing conflicts.
Unavailability of laundry facilities.
Inconvenient visiting hours for family and friends.
Poor maintenance of hostel buildings.
Unresponsive hostel staff.
No clear policies for room allocation or transfer requests.
Long queues for meals during peak hours.Lack of proper storage space for personal belongings.
No designated study areas in the hostel.
Inefficient complaint redressal mechanism for hostel-related issues.
Delay in responding to maintenance requests for broken facilities.
Lack of clarity on hostel accommodation policies for postgraduate students.
Insufficient guidelines for students regarding hostel safety and security.""",
#CHUNK8 data
""" GRIEVANCES: No availability of transportation options to and from the hostel.
Hostels not being adequately cleaned after events or parties.
No flexibility in checking out during holidays or vacations.
Inadequate provision of basic toiletries (soap, toilet paper, etc.).
Restricted or limited access to electricity sockets.
Unreasonable curfew timings for hostel entry.
Poorly maintained windows or doors.
Inconsistent water supply for showers or cleaning.
Hostels not allowing guests of the opposite gender.
No proper grievance redressal system for hostel issues.
Difficulty in getting accommodation during peak seasons.
Inconvenient or poorly managed mess timings.
Issues with the cleanliness of common areas like lounges.
Lack of proper fire exits or emergency evacuation plans.""",

#chunk9 data
"""GRIEVANCES:Unclear policies for hostel fee refunds or adjustments.
Problems with hostel management handling special accommodation requests.
No proper trash collection or waste segregation systems.
No designated areas for bike or vehicle parking.
Hostels not being able to accommodate students during holidays.
Long waiting times for hostel maintenance requests.
Lack of transparency in hostel fee structure.
Poor quality of mattresses or bedding.
Limited access to medical facilities or first aid kits in the hostel.
Hostels having inconsistent guest policies.
Issues with hostel gates or access control systems.
Insufficient safety or security personnel in the hostel.
Poor behavior or rudeness from hostel staff.
Lack of access to emergency medical services.
Unhygienic conditions in the hostel kitchen.
""",

#chunk 10 data
"""GRIEVANCES:Hostels not offering enough parking space for students with cars.
Poorly managed waste disposal in and around the hostel.
No clear instructions on how to request repairs or maintenance.
Unavailability of bed linens or room cleaning services.
Lack of study materials or hostel library resources.
Noise issues due to construction or other external factors.
No provision for ensuring pest control in the hostel.
Poor quality or inadequate hostel bedding or linens.
Uncomfortable room layouts or poor space management.
Inadequate lighting in common areas such as hallways.
Lack of privacy for students in shared rooms.
Difficulties with getting a roommate change or transfer.Unclear or unreasonable rules regarding hostel check-ins and check-outs.
Problems with heating systems in cold weather.
Slow response times to complaints or requests to the hostel office.
""",

#chunk 11 data
"""GRIEVANCES: Poor attitude of fellow students causing conflicts or disturbances.
Restrictions on personal items (e.g., no cooking appliances allowed).
Limited opportunities for recreational or social activities.
Lack of outlets or charging points for electronic devices.
Inability to accommodate students with special needs or disabilities.
Difficulty in availing late-night entry for students with evening classes.
Overcrowded dining facilities leading to long waiting times for meals.
No provision for early check-in or late check-out during exams.
Insufficient bedding for extra students or temporary accommodation.
Inconsistent or unreliable heating systems during winter.
Unclear communication regarding hostel rules and regulations.
No backup power supply during power outages.
Inadequate or inaccessible storage spaces for luggage or personal items.
No privacy for phone calls or conversations in the hostel.
Hostels being too far from campus or academic buildings.
Overly restrictive visiting hours for parents or guardians.
""",

#chunk12 data
"""GRIEVANCES: Mismanagement of hostel reservation during special events or peak seasons.
No access to recreational or fitness areas like gyms.
Problems with payment methods or payment systems for hostel fees.
Unclear or missing policies for hostel breakages or damages.
Inconsistent standards of cleanliness across different hostels.
Lack of representation or student body to voice hostel-related issues.
Poor quality of food in the hostel mess.
Frequent breakdown of water supply in hostels.
Unavailability of sufficient electricity during peak hours.
No provision for vegetarian food in the hostel.
Lack of maintenance of common areas like lounges and corridors.
Poor quality of bed linens and blankets.
Irregular cleaning of hostel bathrooms.
Unavailability of dustbins or waste bins in rooms and corridors.
Unhygienic conditions in the hostel kitchen.
Lack of storage space for students' personal belongings.
Hostels with inadequate security measures.
Unclear policies regarding guest entry in hostels.
Insufficient recreational facilities such as TV or games.No study rooms or quiet areas for students to work.
Unfriendly or unhelpful hostel staff.
Constant power outages affecting room comfort.
Insufficient water pressure for showers and cleaning.
Inadequate heating during winter months.
""",

#chunk13 data
"""GRIEVANCES: LNoise disturbances from other rooms or outside the hostel.
No provisions for students with special dietary requirements.
Lack of cleanliness in common areas such as lounges and dining halls.
Overcrowded rooms with too many students assigned to them.
Slow or inefficient room allocation process.
No privacy in shared rooms.
Lack of proper ventilation leading to stuffy rooms.
No safety equipment like fire extinguishers or alarms.
Inefficient complaint resolution system for hostel-related issues.
Inadequate lighting in hostel rooms and common areas.
Long queues for meals during peak hours.
No availability of proper laundry services.
Unfair room allocation process without clear criteria.
Lack of a proper waste segregation system for recycling.
Unclear rules on room switching or changing roommates.
Insufficient or outdated furniture in rooms.
Lack of access to public transportation to and from the hostel.
Inconsistent Wi-Fi connectivity throughout the hostel.
No system in place for resolving roommate conflicts.
No backup power during power outages.
Issues with hostel maintenance requests not being attended to in time.
Lack of necessary kitchen equipment for students who want to cook.
Poor cleanliness standards in hostel dining areas.
Inadequate privacy in the hostel washrooms or showers.""",

#chunk 14 data
"""GRIEVANCES: Difficulties with booking or accessing common facilities.
Poorly maintained parking facilities for students' vehicles.
Unclear procedures for checking in and checking out of the hostel.
Lack of support for students with medical or psychological needs.
Restrictive hostel timings for students with evening classes or jobs.
No clear guidelines regarding the return of hostel keys or documents.
No clear policies regarding the maintenance or replacement of damaged items.
No monitoring of noise levels during late-night hours.
No provision for early or late check-ins during exams or special events.
Delayed responses from hostel management to urgent issues.
Unclear policies regarding the hostel fee refund process.
Insufficient fire exits or emergency evacuation plans.
Unclear policies on overnight stays for family or friends.
Lack of safety measures in hostel buildings.
Delayed allocation of rooms at the start of the academic year.
Poor management of hostel check-in and check-out procedures.
Problems with hostel administration handling requests for extended stays.
No proper seating arrangements in common areas.
Lack of proper facilities for waste disposal or recycling.
""",
#chunk15 data
"""Inconsistent availability of laundry services or machines.
Problems with excessive noise from construction near hostels.
Overcrowded dining halls leading to long wait times for meals.
Inconsistent water supply in certain hostel blocks or areas.
Lack of students' input in hostel management decisions.
Unclear or inadequate guidelines for hostel fee payments.
Unfair or discriminatory room allocation based on non-transparent criteria.
Inadequate supply of toiletries in the hostel.
Inefficient handling of emergency situations in hostels.
Insufficient number of rooms for students during peak admission times.
Problems with the cleanliness and hygiene of hostel corridors.
No flexibility in terms of late-night access to hostel gates.Issues with getting necessary medical assistance or access to first aid.
Limited access to printing or photocopying services.
Inadequate ventilation in the hostel dining room.
Problems with excessive billing for hostel services or utilities.
No access to outdoor spaces or sports facilities.
Inefficient management of complaints or suggestions submitted by students.
Poorly managed or unavailable shuttle services to and from campus.
Problems with the assignment of rooms during festivals or holidays.
""",
#chunk 16 data
"""Lack of student involvement in the decision-making process for hostel improvements.
Unclear policies for accommodation during mid-semester breaks.
Lack of online booking or room reservation options.
No clear policy for reimbursement of hostel fee overcharges.Difficulty in communicating with hostel staff regarding urgent issues.
Lack of proper signage or instructions for hostel guests or newcomers.
Inadequate infrastructure for wheelchair-bound students or disabled individuals.
Delay in providing necessary hostel documentation like receipts or certificates.
Hostels being located far from academic buildings or campus facilities.
Unclear rules regarding bringing pets into the hostel.
Inconsistent enforcement of cleanliness standards by hostel staff.
Lack of access to emergency contacts or phone numbers for hostel issues.
Issues with the hostel's waste management and sanitation practices.
Inadequate provision of basic amenities like towels, soaps, etc.
Lack of storage facilities for luggage during holidays.
Problems with maintaining cleanliness in shared or communal spaces.
"""
]

department_id = "Hostel Department"

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
