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
    """Electrical Maintenance Department in College:Overview:The Electrical Maintenance Department in a college is crucial for ensuring the safe, efficient, and uninterrupted operation of all electrical systems on campus. This department is responsible for the installation, inspection, maintenance, and repair of electrical infrastructure, ensuring
    compliance with safety regulations and minimizing potential hazards. It plays a vital role in supporting academic activities by maintaining power supply, lighting, and equipment essential for classrooms, laboratories, and hostels.Key Responsibilities of the Electrical Maintenance Department: Power Supply Management:Ensures a steady and uninterrupted 
    power supply to all college buildings, including classrooms, laboratories, offices, hostels, libraries, and auditoriums.Monitors and maintains main distribution panels, transformers, circuit breakers, and power generators.Manages load distribution to prevent power fluctuations and outages.Lighting System Maintenance:Regularly checks and maintains lighting 
    fixtures in classrooms, corridors, outdoor areas, and parking lots.Replaces damaged bulbs, tube lights, and LED fixtures promptly.Implements energy-saving measures such as LED installations and sensor-based lighting systems.Electrical Equipment and Appliances Maintenance:Conducts routine inspections and servicing of electrical appliances such as fans, air 
    conditioners, refrigerators, water coolers, laboratory equipment, and computers.Ensures safe wiring and power connections for all electrical devices used in academic and administrative activities.Checks UPS (Uninterruptible Power Supply) systems in IT labs to avoid data loss due to power failures.""",
    #chunk-2 data
    """ Key Responsibilities of the Electrical Maintenance Department:Emergency and Fault Handling:Responds immediately to power outages, short circuits, and electrical faults.Conducts fault analysis and root cause assessment to prevent recurring issues.Maintains backup generators and inverters for emergency power supply.Safety and Compliance:Ensures compliance with
    national and local electrical safety regulations (such as IS/IEC standards).Conducts routine safety audits and electrical inspections in hostels, classrooms, and offices.Maintains proper earthing and surge protection systems to prevent electrical hazards.Energy Efficiency and Sustainability:Implements energy conservation measures, including the use of solar panels, 
    energy-efficient appliances, and automation systems.Conducts energy audits to analyze power consumption and reduce wastage.Promotes awareness campaigns on energy efficiency among students and staff.Infrastructure Development and Upgrades:Plans and executes electrical installations for new campus buildings and renovation projects.Upgrades outdated electrical systems 
    to meet increasing power demands and safety standards.Coordinates with civil and mechanical departments for integrated campus infrastructure planning.Coordination with External Agencies:Works closely with government electricity boards, contractors, and suppliers for repairs, maintenance, and new installations.Ensures timely procurement of electrical spare parts and equipment.
    Follows up on pending power connection approvals and regulatory clearances.""",
    #chunk-3 data
    """Guidelines for Students Regarding Electrical Maintenance:To ensure the safety and proper functioning of electrical systems on campus, students must adhere to the following guidelines:General Safety Guidelines:Report Electrical Issues Promptly:Immediately inform the maintenance department or college authorities about power failures, faulty wiring, or damaged switches.Use designated
    complaint registers, online portals, or emergency contact numbers for reporting issues.Do Not Tamper with Electrical Installations:Avoid touching exposed wires, circuit breakers, or power distribution panels.Do not attempt to repair electrical appliances or sockets on your own.Proper Usage of Electrical Appliances:Switch off lights, fans, ACs, and computers when leaving classrooms, hostels,
    or labs to conserve energy.Avoid using high-wattage personal appliances like heaters or electric stoves in hostel rooms unless permitted.Ensure that lab equipment is used according to faculty or technician instructions.Prevent Overloading of Electrical Sockets:Do not plug multiple high-power devices into a single socket as it may cause overheating and short circuits.Use surge protectors and 
    proper extension boards if needed.Awareness of Emergency Procedures:In case of an electrical fire, do not use water; use a fire extinguisher or sand instead.Immediately disconnect the main power supply and evacuate the area if a major electrical fault occurs.Be aware of emergency exit routes and fire safety equipment locations.""",
    #chunk_4 data
    """Guidelines for Students Regarding Electrical Maintenance:Restricted Access Areas:Do not enter transformer rooms, generator areas, or high-voltage sections without authorization.Avoid touching electrical panels, distribution boxes, or underground power cables.Participation in Safety Training & Workshops:Attend safety awareness sessions and electrical maintenance training programs organized by 
    the college.Learn basic electrical safety measures and first-aid procedures for handling electrical accidents.Follow Hostel Electrical Rules:Use only permitted electrical gadgets in hostel rooms.Do not hang wet clothes near electrical outlets or appliances.Ensure that room wiring is intact and avoid using defective extension cords.Encouragement of Sustainable Practices:Support energy-saving initiatives 
    such as switching off unnecessary lights and fans.Participate in eco-friendly campaigns promoting renewable energy sources on campus.The Electrical Maintenance Department plays a vital role in ensuring a safe, efficient, and uninterrupted power supply across the collee campus. By following the provided guidelines, students can contribute to maintaining a safe electrical environment while promoting sustainability 
    and energy conservation. Regular coordination between students, faculty, and the maintenance team ensures quick resolution of electrical issues and enhances campus safety.GRIEVANCES:
    Frequent power outages disrupting classes and hostel activities.
    Voltage fluctuations damaging electronic devices and appliances.
    Sudden power cuts during online classes or lab sessions.""",
    #chunk_5 data
    """GRIEVANCES:Generator backup not functioning properly during power failures.
Delayed response to power outage complaints.
Lighting Problems
Non-functional tube lights and LED bulbs in classrooms.
Insufficient lighting in hostel corridors and staircases.
Flickering lights causing inconvenience in study areas.
Outdoor streetlights on campus not working, leading to safety concerns.
Overhead lighting in labs being too dim or too bright.
Electrical Equipment & Appliance Issues
Faulty fans in classrooms and hostels.
Air conditioners not cooling efficiently in lecture halls.
Water coolers not functioning properly in summer.
Defective projectors and smart classroom equipment due to power issues.
Non-working exhaust fans in washrooms and kitchens.
Faulty Electrical Wiring & Sockets
Loose electrical wires hanging from walls and ceilings.
Exposed electrical wiring in hostels posing safety hazards.
Broken or sparking plug points in classrooms.
Overloaded power sockets leading to short circuits.
Defective or non-functional switchboards in labs and offices.
Emergency & Safety Concerns
Fire hazards due to overheated electrical panels.
No clear emergency protocol for electrical accidents.
Lack of fire extinguishers near electrical installations.
Delayed action on reporting of electrical sparks or short circuits.
Safety measures not implemented for high-voltage areas.
Energy Efficiency & Sustainability Issues
Wastage of electricity due to lights and fans left on in empty classrooms.
Lack of sensor-based lighting in washrooms and common areas.""",
    #chunk_6 data
    """GRIEVANCES:No solar panel installation despite high electricity consumption.
Inefficient power distribution leading to energy wastage.
Lack of awareness campaigns on energy conservation.
Maintenance Delays & Inefficiencies
Long wait times for resolving reported electrical issues.
Maintenance staff not responding promptly to complaints.
Lack of a proper complaint-tracking system for students.
Repeated electrical issues despite previous repairs.
Poor coordination between departments for maintenance tasks.
Hostel-Related Electrical Grievances
Room sockets not working properly for charging devices.
Frequent short circuits in hostel rooms.
Non-functional geysers leading to cold water issues.
Insufficient power points for students to charge their devices.
Unauthorized use of high-power appliances causing circuit overloads.
Lab & IT Infrastructure Issues
Computer lab systems shutting down due to electrical failures.
UPS backup failing during practical sessions.
No proper grounding for electronic lab equipment.
Poor maintenance of networking and IT-related power supply.
Power surges affecting lab experiments and research work.
Streetlight & Outdoor Electrical Concerns
Streetlights remaining on during the day, wasting electricity.
Insufficient lighting around campus roads and parking areas.
Faulty CCTV camera wiring causing security blind spots.
Non-functional emergency alarm system in college premises.
Lack of proper signage for high-voltage electrical areas.
Power cuts during exams disrupting students' concentration.""",
    #chunk_7 data
    """ GRIEVANCES: Delay in replacing damaged ceiling fans.
Inconsistent power supply in computer labs affecting practical sessions.
Non-functional elevators due to electrical faults.
Lack of periodic maintenance checks for electrical equipment.
Generator not turning on automatically during power failures.
High electricity bills due to inefficient power management.
Water pumps frequently stop working due to electrical faults.
Power trips during heavy rains, leaving hostels in darkness.
Defective electrical wiring causing burning smell in corridors.
No proper maintenance schedule for checking electrical panels.
Electrical sockets near water sources not properly insulated.
Loud humming noise from transformers causing disturbance.
Fans making unusual noise due to lack of lubrication.
Exposed junction boxes posing a safety risk.
Frequent electrical shocks from faulty appliances.
No emergency power supply in critical areas like hospitals or medical rooms.
Students not informed about scheduled power outages in advance.
Electric bells in classrooms not working properly.
Lack of surge protection for sensitive lab equipment.
Poor earthing in buildings leading to frequent electrical issues.
Incomplete wiring in newly constructed buildings.
Old and deteriorated electrical infrastructure not being upgraded.
Lack of proper labeling on electrical panels.
Extension cords used excessively due to lack of power outlets.
Lack of maintenance staff availability during weekends.
Non-functional emergency exit lights during power failures.""",
#CHUNK8 data
""" GRIEVANCES: Electrical wiring interfering with network cables.
Unauthorized tampering with electrical installations.
Power supply interruptions in the library affecting students.
Poor quality electrical fittings leading to frequent breakdowns.
Damage to electrical circuits due to rodent infestation.
No proper ventilation in electrical control rooms.
College auditoriums experiencing power failures during events.
No dedicated complaint desk for electrical grievances.
Lack of modern energy-saving lighting solutions.
Defective circuit breakers not being replaced on time.
Electric signboards not working properly.
Electrical issues in faculty rooms affecting administrative work.
High noise levels from old transformers.
College mess equipment frequently breaking down due to power fluctuations.
Smart classroom devices not charging due to faulty wiring.
Use of low-quality electrical materials for repairs.
Some areas experiencing excessive power loads causing fuse failures.
Students using unsafe electrical appliances in hostels due to lack of guidelines.
Shortage of skilled electricians leading to unresolved issues.
Lack of a mobile app or online portal for quick complaint registration.
Frequent complaints about broken electric kettles in hostel common areas.
Improper cable management leading to tangled and hazardous wiring.
No proper backup system for essential security equipment like alarms and biometric attendance systems.
Streetlights inside the campus not functioning properly.
Outdoor lighting too dim, creating safety concerns at night.""",

#chunk9 data
"""GRIEVANCES:Frequent fuse blowouts in classrooms.
Power sockets in labs not supporting high-power devices.
Damaged or loose electrical switches in multiple locations.
No proper system for students to report electrical complaints.
Delays in addressing electrical hazards reported by students.
Lack of training for students on electrical safety.
AC units in lecture halls frequently malfunctioning.
No standby generator for hostel blocks.
Electrical panels left open, posing a serious risk.
Students getting minor shocks from exposed wiring.
Water leakage causing short circuits in certain areas.
High voltage fluctuations damaging student laptops.
Fan regulators not working properly in classrooms.
Classroom tube lights flickering continuously.
Projector screens failing to retract due to power issues.
Insufficient number of charging ports in the library.
Hostel corridors having non-functional lights.
Washing machines in hostels experiencing frequent power failures.
Power backup taking too long to restore supply during outages.
Electric kettles and microwaves in hostels frequently tripping circuit breakers.
Lack of clear safety instructions near electrical installations.
Insufficient maintenance staff to handle emergency breakdowns.
Faulty CCTV cameras due to irregular power supply.
Loud buzzing noise from electrical transformers.
No night-time maintenance team for urgent repairs.
Voltage dips affecting high-tech equipment in research labs.
Fire alarms failing to function during testing.
Water coolers frequently shutting down due to electrical faults.""",

#chunk 10 data
"""GRIEVANCES:Lack of accessible power sockets in auditoriums for presentations.
Unused electrical appliances consuming unnecessary power.
Students using excessive extension cords due to lack of direct connections.
No warning signs near areas with high-voltage equipment.
Overheating of electrical wires leading to minor fire incidents.
Burnt-out bulbs not being replaced on time.
Power issues affecting attendance biometric systems.
AC drainage pipes leaking onto electrical wiring.
Noise pollution from old generators.
Delays in replacing damaged fan blades.
Improper disposal of old electrical components.
Exposed wiring in student activity areas.
Poor coordination between maintenance staff and student complaints.
No provision for students to report real-time power failures.
Electrical maintenance team not responding to hostel complaints promptly.
Lack of separate circuits for high-power lab equipment.
Unsafe electrical repairs being conducted without proper safety gear.
Lack of solar panels to reduce dependency on grid electricity.
Electric water heaters in hostels frequently malfunctioning.
Maintenance records not being updated properly, causing repeat issues.
Flickering lights in the study halls distracting students.
Electrical switchboards getting overheated in classrooms.
Delay in fixing short circuits in hostel rooms.
No proper earthing in electrical installations, causing minor shocks.
Frequent power outages during peak study hours.
Smart boards in classrooms not functioning due to power issues.""",

#chunk 11 data
"""GRIEVANCES: Low-power backup duration affecting ongoing lab sessions.
Hostel bathroom lights not working, making it unsafe at night.
Sudden power cuts during important college events.
Broken or non-functional exhaust fans in hostel bathrooms.
Computer lab power sockets loose, causing connectivity issues.
Surge protectors in the library not working properly.
Electrical appliances in the canteen frequently shutting down.
Lack of proper insulation in underground wiring.
Electrical panels making a loud humming noise.
Lack of adequate lighting in staircases.
Water heaters in hostels taking too long to heat up due to faulty wiring.
Power fluctuations causing audio systems to malfunction during lectures.
Emergency exit signs not illuminated due to faulty circuits.
No clear emergency response plan for electrical failures.
Ceiling fans producing excessive noise in classrooms.
No proper maintenance of solar lights installed on campus.
Microwave ovens in hostels getting frequent power failures.
No proper power distribution causing uneven load on circuits.
Circuit breakers frequently tripping in academic blocks.
Lack of proper ventilation in electrical rooms, causing overheating.
Lack of energy-efficient electrical solutions on campus.
College auditorium lights taking too long to turn on.
Poor communication between maintenance team and students about repair schedules.
High electric bills due to inefficient power usage monitoring.
Lack of accessibility for disabled students in electrical facility areas.""",

#chunk12 data
"""GRIEVANCES: Students using unauthorized electrical appliances due to insufficient facilities.
ACs not cooling effectively due to inconsistent power supply.
High-intensity LED lights in reading rooms causing eye strain.
Water-damaged electrical panels not being replaced on time.
Extension cords being overused, leading to potential hazards.
No proper inspection of old wiring in older buildings.
Lack of safety barriers around high-voltage transformers.
Electrical sockets placed too high, making them difficult to access.
Difficulty in getting approval for student-installed electrical equipment.
Worn-out insulation tape on exposed wires.
Electrical equipment in sports complex not maintained regularly.
Irregular testing of fire and smoke alarms in labs.
No proper locking system for electrical maintenance rooms.
Lighting in parking areas insufficient, causing security concerns.
Elevator malfunctions due to unstable power supply.
High noise levels from electrical generators disrupting classes.
Emergency lights in corridors not functional during power failures.
No signage indicating high-voltage zones.
Delay in replacing broken power cables affecting multiple buildings.
Frequent power outages in hostel rooms.
Flickering tube lights in multiple rooms.
Electrical sockets not working in some rooms.
Ceiling fans making excessive noise.
Room light switches getting stuck or not functioning.
Low-voltage issues affecting charging speed of devices.
Power fluctuations causing laptop and mobile charging failures.""",

#chunk13 data
"""GRIEVANCES:AC units in hostel rooms not cooling properly.
Water heaters taking too long to heat up.
Electrical shocks from bathroom geysers.
Exhaust fans in bathrooms not working.
Corridor lights not working at night.
Hostel common room TV frequently losing power.
Washing machines stopping due to power issues.
Frequent tripping of circuit breakers in rooms.
Poor placement of electrical switches, making them hard to access.
Refrigerator sockets in common areas not functioning.
Broken plug points in study rooms.
Lights outside hostel entrance not turning on.
Emergency exit signs not illuminated.
Water coolers frequently losing power.
Inconsistent power supply affecting hostel Wi-Fi routers.
Extension cords being overused due to insufficient power points.
Overheating electrical panels in hostel corridors.
No proper maintenance of inverter batteries for backup power.
Electric kettles causing frequent power trips in rooms.
Electrical wiring exposed in some hostel rooms.
No emergency lights during power failures.
Power supply issues affecting induction stoves in mess areas.
Lack of proper insulation on wiring under beds and tables.
Overloading of hostel power lines due to excessive use of high-power devices.
Loose or broken switchboards in hostel rooms.
Lights in the study hall frequently turning off.
Hostel elevator malfunctioning due to power issues.
Noisy electrical transformers near hostel rooms.
High electric bills due to inefficient hostel power management.
Some rooms experiencing continuous dim lighting.""",

#chunk 14 data
"""GRIEVANCES: Lack of surge protectors in hostel rooms.
Malfunctioning motion-sensor lights in hostel corridors.
Delay in repairing faulty electrical appliances in common areas.
Unstable power supply in hostel security cabins.
Inverter backup duration too short during long power cuts.
High voltage in some rooms causing appliance damage.
Noisy generator placed near hostel rooms.
Electric shock risk from rusted switchboards.
Lack of proper lighting around hostel parking areas.
Exposed wires in hostel terrace areas.
Switchboards sparking when plugging in devices.
Faulty wiring in hostel mess causing frequent short circuits.
Lack of maintenance for hostel intercom electrical connections.
Hostel CCTV cameras frequently losing power connection.
Burnt smell from old electrical wiring.
Hostel maintenance staff taking too long to respond to complaints.
LED lights flickering in hostel staircases.
Lack of backup generators for hostel power cuts.
Limited charging points causing inconvenience for students.
Unauthorized electrical modifications by students increasing risks.
Hostel water purifiers stopping due to power fluctuations.
Faulty AC stabilizers causing cooling inefficiencies.
Hostel printers in common areas shutting down frequently.
Refrigerators in hostel common areas not cooling properly due to power issues.
Microwave ovens frequently shutting off in hostel pantry.
Defective MCBs (Miniature Circuit Breakers) causing blackouts in certain blocks.
Poor earthing in hostel leading to minor electric shocks.""",
#chunk15 data
"""GRIEVANCES:Students using illegal high-power devices causing overloads.
Power tripping when multiple students use hair dryers.
Lack of night lamps in hostel rooms.
Weak electrical support for hostel study desks.
Circuit panel covers missing, exposing live wires.
Hostel speakers in common areas not working due to power issues.
Fans running at variable speeds due to voltage fluctuation.
Malfunctioning temperature controllers in hostel geysers.
Mess hall lighting too dim, affecting visibility.
Loose electrical joints causing intermittent power failure.
Hostel corridor lights staying on even during the daytime.
Inconsistent power backup between different hostel blocks.
Damaged insulation on hostel room wiring.
Difficulty in getting approval for student-installed extension boards.
Poor wiring affecting hostel computer lab power stability.
Water leakage near hostel electrical installations.
Power supply to hostel rooftops affecting solar panel efficiency.
Certain hostel rooms experiencing random power failures.
Delayed repair of hostel generator failures.
High wattage lights causing excessive heat in rooms.
Motion-sensor lights in washrooms not detecting movement correctly.
Safety hazard from improperly installed power strips.
No power outlets near hostel study desks.
Lack of timely inspection for outdated hostel wiring.
Unstable power supply affecting hostel washing machines.
Faulty electric bells in hostel entrance gates.
Hostel geysers not turning off automatically after heating.""",
#chunk 16 data
"""GRIEVANCES:No proper markings on electrical panels for safety.
Voltage fluctuation causing hostel fans to slow down unexpectedly.
Certain hostel sections facing longer power outages than others.
Students tampering with electrical wiring causing maintenance issues.
Hostel switchboards having fake grounding, causing safety risks.
Irregular maintenance of electrical installations in older hostel buildings.
Frequent fire alarm malfunctions due to power failures.
Lack of awareness about electrical safety protocols among hostel students.
Unavailability of emergency contact numbers for electrical maintenance staff."""
]

department_id = "Electrical Maintenance Department"

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
