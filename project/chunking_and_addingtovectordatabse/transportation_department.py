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
    """Transportation Department: Overview and Guidelines Description: The Transportation Department manages and oversees all transportation-related services within the college, ensuring safe, efficient, and punctual travel for students, faculty, and staff. It coordinates bus routes, schedules, vehicle maintenance, and transport safety regulations. The department also addresses 
    transportation-related grievances, ensuring smooth commuting experiences for the college community.Key Responsibilities of the Transportation Department: College Bus Services: Organizes and manages the fleet of college buses, ensuring timely pick-ups and drop-offs.Route Planning: Designs bus routes to cover major areas while optimizing travel time and fuel efficiency.Safety and 
    Compliance: Ensures that all vehicles meet safety standards and that drivers follow traffic regulations.Maintenance and Repairs: Regularly inspects and maintains buses and other college-owned vehicles.Transport Pass Issuance: Issues transport passes or ID cards to students and staff using college transport.Emergency Transport Services: Provides vehicles in case of medical or 
    other emergencies on campus.Grievance Handling: Addresses complaints related to transport delays, safety concerns, and bus overcrowding.Eco-Friendly Initiatives: Encourages sustainable transport options like carpooling or electric buses.""",
    #chunk-2 data
    """ Guidelines for Students to Follow: Adhere to Bus Timings: Arrive at bus stops on time to avoid delays for other passengers.Carry Your Transport Pass: Always keep your transport ID or pass handy for verification.Follow Seating Arrangements: Do not occupy reserved seats or create disturbances during travel.Respect Bus Staff and Drivers: Treat drivers and transport staff with 
    courtesy and follow their instructions.Report Issues Promptly: Inform the transportation office if you experience delays, mismanagement, or vehicle malfunctions.Avoid Littering: Keep the buses clean and dispose of waste properly.Use Bus Services Responsibly: Do not engage in unsafe behavior like standing in moving buses or blocking exits.Follow Safety Protocols: Use designated bus stops, 
    avoid unnecessary standing, and do not lean out of windows.Do Not Distract Drivers: Avoid loud music, shouting, or behavior that may distract the driver.Inform About Route Changes in Advance: If you need a change in your transport route, submit a request with valid reasons to the transport office.GRIEVANCES:Delayed arrival of university buses during peak hours.
Insufficient number of buses to accommodate all students.
Buses not following the designated routes or schedules.
Unavailability of transport options during late-night hours.
Overcrowding in buses, especially during rush hours.""",
    #chunk-3 data
    """GRIEVANCES: Poor condition of buses (broken seats, lack of ventilation).
No updates on bus delays or cancellations.
Lack of proper maintenance of university vehicles.
No shuttle services to off-campus locations.
Inconsistent timing of transport services, leading to missed classes.
Buses being overcrowded with staff and faculty, leaving students without space.
No provision for students with special needs in transportation services.
No real-time tracking of buses for students to know when they will arrive.
No proper signage at bus stops, causing confusion.
Delays in the pickup or drop-off of students from hostels.
Unsafe or poorly lit bus stops on campus or nearby areas.
Transport services being canceled without prior notice.
Lack of seating capacity for long-distance travel to off-campus locations.
No dedicated transportation services for students with exams or academic events.
No access to transport during inclement weather conditions.
Lack of clear communication about transport schedules during holidays.
Students not being informed about changes in bus routes or timings.""",
    #chunk_4 data
    """GRIEVANCES:No flexibility in transport schedules for students working late or attending extracurricular activities.
Transport services often running late without an explanation.
No online platform to report transportation-related issues.
Drivers being rude or unprofessional during travel.
Unavailability of transport services on weekends or public holidays.
High transport fares with no clear justification for price hikes.
Limited seating options for students with long-distance commutes.
Lack of timely transportation for students attending early morning exams.
No proper cleanliness maintained in buses (e.g., garbage, dirty seats).
No tracking system for lost belongings in transportation.
Not enough buses to serve all student hostels, resulting in delays.No provision of air-conditioned buses for students during summer months.
Difficulty in getting transport tickets or passes due to lack of clarity on the system.
Long waiting times for buses during non-peak hours.
Inadequate bus services for students living in more distant areas.
No separate transport service for female students, leading to safety concerns.""",
    #chunk_5 data
    """ GRIEVANCES: Lack of bus facilities for students with heavy luggage (e.g., for field trips or events).
Limited transport options for students needing to attend off-campus internships.
No proper system to notify students about changes in transport schedules due to weather conditions.
Overcharging for transport passes or tickets for short-distance trips.
No direct transport route between key campus locations and nearby housing areas.
Students facing difficulty in getting transport in the evening due to increasing demand.
Lack of safety measures such as seatbelts in university buses.
No emergency contact system for students facing issues with transportation.
No timely communication about transport service changes during exam or vacation periods.
No provision of safe transport for female students late at night.
No real-time updates on bus location or estimated arrival times.
Transport services not being available during national or regional holidays, affecting students' travel plans.
Buses taking longer routes, causing unnecessary delays.
Lack of transportation for students attending evening classes or events.
No bus services for students living in rural or less accessible areas.
Poorly maintained roads leading to transportation delays.
Drivers not following speed limits or driving recklessly.
No clarity on the process of booking transportation for group activities or field trips.
No transport facilities for students attending off-campus workshops or conferences.
Difficulty in accessing transportation for students with medical conditions.""",
    #chunk_6 data
    """GRIEVANCES:Students not being informed about changes in transport routes due to construction or roadwork.
No dedicated transport services for students with part-time jobs or internships.
Excessive travel time due to limited bus stops between campuses and student residences.
Buses lacking proper safety equipment like first-aid kits or fire extinguishers.
No updates on expected arrival times for buses during peak hours.
No provisions for late-night transport after extracurricular events or social activities.
Students waiting for buses that do not arrive on time, leading to missed classes.
Poor communication regarding transport services during special events or holidays.
Buses with broken air-conditioning systems, making them uncomfortable.
Limited seating for students with heavy academic materials (books, project work, etc.).
Lack of bus facilities for students attending off-campus exams.
No online booking system for students to secure their seats in advance.
No transport services for students living in newly constructed housing areas.
Limited number of buses during exam season, leading to overcrowding.
Lack of coordination between transport services and university events
Buses having no designated routes for students traveling from hostels to academic buildings""",
    #chunk_7 data
    """ GRIEVANCES: Insufficient number of buses to cater to students during peak hours between classes.
No system in place to notify students in advance if a bus will be delayed or canceled.
Poor lighting and visibility at bus stops, especially in the evening.
Lack of convenient drop-off locations near academic buildings.
No shuttle services for students attending off-campus internships or jobs.
Students being charged additional fees for special transport services (e.g., field trips, workshops).
No provision for student transport during special campus events or exams held off-campus.
Limited transport options for students needing to return home during semester breaks.
No coordinated schedule between transport services and class timings.
Students unable to travel long distances due to the unavailability of express buses.
Lack of cleanliness and maintenance of buses, leading to unpleasant travel experiences.
No transparency in bus scheduling, leaving students unsure about bus timings.
Difficulty in getting transport for students attending conferences or research events off-campus.
No weekend transport options for students needing to travel home or for personal activities.
Transport services running late due to inefficient traffic management near the campus.
No arrangement for group travel for students attending academic conferences or seminars.Students having to wait long hours for the next available bus during off-peak hours.
No student-friendly transportation options available for attending part-time evening courses.
Inconsistent transport schedules during exam periods, causing inconvenience.""",
#CHUNK8 data
""" GRIEVANCES: Lack of transportation for students attending late-night lab work or research.
No transport facilities for students attending cultural or sports events organized by the university.
No notification about bus delays on the university's official transportation app or website.
Poor accessibility of transport for students with physical disabilities.
Not enough buses available for students to attend off-campus workshops, lab work, or site visits.
Inadequate bus parking or pickup/drop-off spaces near university buildings.
Transport services not being equipped to handle peak load during orientation or welcome weeks.
No clarity on the process for students to reserve seats during peak hours.
Unreliable bus services causing students to arrive late for classes or exams.
Inconvenient bus stop locations, requiring students to walk long distances.
Lack of real-time notifications about bus cancellations or delays.
No bus services for students working late shifts at the university.
Inconsistent service during semester breaks or holidays.
Bus drivers not following the designated stops or routes.
Insufficient buses available during peak traffic hours.
Difficulty in contacting transportation staff in case of emergencies.
No communication about bus services during weather-related closures.""",

#chunk9 data
"""GRIEVANCES:Unclear process for obtaining transport passes or tickets.
No transport services available for students attending evening extracurricular activities.
Buses becoming overcrowded due to lack of seating capacity.
Students being forced to stand in buses for long durations due to full seating capacity.
Transport facilities unavailable for students attending weekend classes.
Lack of provisions for student-friendly transportation, like discounted fares or passes.
Transport services running late due to mismanagement of routes.
Inadequate transport options available for students from remote hostels.
Frequent breakdowns of buses causing delays.
No clear procedure for students to request transport during emergency situations.
Students being overcharged for long-distance transportation services.
Lack of safe and secure transport for female students late at night.
No coordination between the transport schedule and students’ class timings.
Inadequate parking facilities for buses, causing congestion and delays.
No transportation options for students attending research or off-campus academic sessions.
Long waiting times for buses due to insufficient frequency during off-peak hours.
Lack of direct routes between popular student areas and the university.
Overcrowded buses leading to a lack of social distancing or ventilation.
No clear system for communicating transport changes due to university events or activities.
No online platform for students to provide feedback about transportation services.""",

#chunk 10 data
"""GRIEVANCES:Difficulty in obtaining transport due to limited availability during exam times.
Poor visibility of bus schedules at bus stops.
Limited late-night transport options for students studying in libraries or labs.
No transport services for students during national holidays.
Lack of eco-friendly transport options like electric buses or bicycles.
Unclear pricing structure for short-distance and long-distance student transport.
No options for group transport for students attending conferences or group fieldwork.
Inconsistent or unclear timing of shuttle services for large events or orientations.
Students waiting for long periods due to bus delays without prior notice.
No provision for students with special requirements, such as carrying heavy academic materials or equipment.
Lack of coordination between transportation and campus security, causing safety concerns.
Transport not operating during campus strikes or protests, leaving students stranded.
Inadequate bus services for students from neighboring cities.
Limited routes available for students attending off-campus study sessions.
Unclean buses with inadequate sanitation facilities.
Lack of proper signage for bus routes and schedules at off-campus transport points.
No transparency about the availability of transport during emergency situations like natural disasters.
No provision of transport for students attending post-graduation ceremonies or special events.
Students experiencing issues due to the unavailability of buses on festival days.
Difficulty in getting transport due to confusion over booking systems or unclear instructions.""",

#chunk 11 data
"""GRIEVANCES: Lack of transportation services for students attending special university events.
Unclear or inconsistent bus schedules during exam periods.
No direct routes to specific university buildings or research centers.
Insufficient transport during the beginning and end of semesters when student numbers are high.
Inconsistent or delayed bus arrivals, leading to uncertainty for students.
No emergency transport services for students during unexpected situations.
Long commute times due to multiple stops for a single route.
Overcrowding during peak hours causing discomfort and delays.
No late-night bus services for students with evening or weekend classes.
No affordable transport options for students without a personal vehicle.
Inconvenient bus routes that require long walking distances to get to campus.
Lack of flexible transport options for students with irregular schedules.
Problems with the transport app not updating real-time bus locations.
No dedicated transport for students attending off-campus internships.
Transport options becoming unavailable due to roadblocks or strikes.""",

#chunk12 data
"""GRIEVANCES: No transport service for students attending workshops, competitions, or exhibitions.
No options for reliable transportation to off-campus events or activities.
Difficulty in booking transport for large groups of students for field trips.
Unavailability of transport during public holidays affecting students’ travel plans.
No shuttle buses to nearby off-campus hostels or student housing.
Buses not adhering to the designated departure times, leaving students waiting for long periods.
No communication regarding sudden route diversions due to construction or accidents.
Unreliable transport services causing students to miss important academic or extracurricular events.
No advance notification about canceled bus services on days with unexpected weather conditions.
Difficulty in accessing transportation due to lack of wheelchair accessible buses.
Students being forced to wait in unsafe conditions at poorly lit or poorly maintained bus stops.
Lack of coordination between public transport services and the university's transportation schedule.
Unavailability of buses during late-night study sessions or research work.
Poor communication when buses are late or running behind schedule.
No shuttle services for students with early-morning exams or events.
Unclear policies regarding free transport for students with financial aid or scholarships.
Lack of alternative transport options for students living in areas with no bus coverage.
Students unable to reach off-campus venues due to the absence of transport options.
Transport service charges being higher than the services provided. """,

#chunk13 data
"""GRIEVANCES: Delayed responses from transportation staff when students have complaints or issues.
No provision of transport for students needing to carry large equipment or materials for projects.
Poor scheduling of transport during orientation periods or campus-wide events.
Inconsistent transport availability during summer and winter breaks.
No system in place to allow students to track buses in real-time.
Lack of public transport integration with the university’s internal transport system.
Buses often not stopping at the correct stops due to confusion about their route.
Insufficient transport for students during the final exam season when extra buses are needed.
Lack of transport availability for students attending late-night university events or social functions.
Overcrowded buses in the evening, making it difficult to find space to travel back to hostels.
Long waiting times for buses during high-traffic periods on campus.
Disorganized transport schedules leading to students missing classes or appointments.
Not enough buses to meet the high demand during orientation or new student intake periods.
No system in place to accommodate emergency transport needs during campus-wide events.
Lack of coordination between the university’s transportation service and local city transport systems.
Transport services not being available during severe weather conditions, such as heavy rain or snow."""

]

department_id = "Transportation Department"

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
