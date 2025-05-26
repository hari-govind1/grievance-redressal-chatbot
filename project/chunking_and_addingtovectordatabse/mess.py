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
    """ Overview of Cafeteria or Mess and Key Responsibilities: Overview of Cafeteria or Mess:The cafeteria or mess in a college serves as a key facility for providing students with meals, snacks, and beverages throughout the day. It is not only a place to eat but also a space for students to socialize, relax, and take breaks between classes. 
    The quality, hygiene, and punctuality of food service are critical in ensuring a good student experience. The cafeteria or mess typically offers a variety of food items, catering to different dietary preferences and needs. Regular maintenance, cleanliness, and food safety are essential aspects that are managed by the staff in charge.
    Key Responsibilities of Cafeteria/Mess Staff:Food Preparation and Quality: Ensure food is prepared in a clean and hygienic environment, maintaining quality and nutritional standards.Menu Management: Design and rotate menus that cater to a variety of tastes and dietary requirements (e.g., vegetarian, vegan, gluten-free).Food Safety and Hygiene:
    Adhere to food safety guidelines and regulations, ensuring proper storage, handling, and serving of food.Timely Service: Ensure meals are served on time, especially during peak hours such as breakfast, lunch, and dinner.Customer Feedback: Collect feedback from students to continuously improve the quality of food and services.Staff Training: Provide ongoing 
    training to cafeteria staff on food safety, customer service, and efficient meal service.""",
    #chunk-2 data
    """ Guidelines for Students to Follow in the Cafeteria/Mess:Maintain Cleanliness: Dispose of used plates, cups, and utensils in the designated bins after eating.Keep the dining area clean by wiping the table if necessary.Respect Timings:Follow the cafeteria schedule for meal timings to avoid crowding during peak hours.Be considerate of the staff and other 
    students when the cafeteria is busy.Food Waste Management:Take only what you can finish to reduce food waste.If you’ve accidentally taken too much, try to leave some food rather than wasting it.Be Considerate of Others:Share tables during busy times and be mindful of others' need for seating.Wait your turn in the food line patiently.
    Follow Dietary Preferences:If you have specific dietary restrictions or preferences, ensure you choose foods that align with them.Notify the cafeteria staff about any special food requirements in advance.""",
    #chunk-3 data
    """Guidelines for Students to Follow in the Cafeteria/Mess : Avoid Disruptive Behavior:Keep noise levels down to create a comfortable dining environment for all.Respect the privacy and space of fellow students.
    Use of Equipment:Handle cafeteria equipment such as trays, cutlery, and beverage machines carefully.Report any broken or malfunctioning equipment to the staff immediately.Provide Feedback:If you have any suggestions, 
    complaints, or appreciation, share your feedback in a constructive manner.Participate in surveys or feedback forms when available to help improve the cafeteria service.
    Payment and Billing:Ensure you make payments for your meals according to the cafeteria’s billing system.Report any billing discrepancies or issues to the cafeteria staff.""",
    #chunk_4 data
    """GRIEVANCES:Food quality is poor and inconsistent.
Limited variety in the menu, leading to repetitive meals.
Unhygienic kitchen and dining areas.
Overpriced food compared to quality and quantity.
Food served is often stale or not fresh.
Unavailability of healthy or nutritious meal options.
Insufficient seating capacity in the cafeteria during peak hours.
Mess staff behaving rudely with students.
Food often being too oily, spicy, or bland.
Poor sanitation, leading to pest infestations like cockroaches and rats.
Inadequate drinking water supply in the dining area.
No proper waste disposal system, leading to bad odors.
Limited options for vegetarian and vegan students.
No accommodation for students with dietary restrictions or allergies.
Meals not being served on time, causing inconvenience.
Insufficient serving portions, leaving students hungry.
Frequent power cuts affecting food preparation and storage.
Dirty utensils and plates provided to students.
No proper queue system, leading to chaos during meal hours.
""",
    #chunk_5 data
    """ GRIEVANCES: Limited meal options on weekends and holidays.
No flexibility in meal plans for students with different schedules.
Lack of refrigeration leading to spoiled food items.
Non-functional fans or air conditioning making the dining area uncomfortable.
Unavailability of fresh fruits and dairy products.
No transparency about food preparation standards and hygiene inspections.
Frequent changes in food suppliers leading to inconsistency in quality.
Food poisoning cases due to unhygienic handling of food.
No special meals for students fasting or following religious dietary restrictions.
Unavailability of non-spicy or less oily food options.
Mess staff not wearing gloves or hairnets while handling food.
Limited operating hours, making it difficult for students with late classes.
No alternative options for students who do not like the regular menu.
No proper ventilation in the kitchen, causing excessive smoke and heat.
Overcrowding during peak hours making it difficult to eat peacefully.
Delay in replenishing food items when they run out.""",
    #chunk_6 data
    """GRIEVANCES:Unavailability of packed or takeaway food for students in a hurry.
No clear labeling of food ingredients for those with allergies.
Food wastage due to inefficient portion control by staff.
Drinking water having an unpleasant taste or being unfiltered.
Non-functional vending machines for snacks and beverages.
No proper handwashing facilities near the dining area.
No variety in breakfast options.
Unavailability of microwaves for students to heat their own food.
No emergency medical support in case of food-related health issues.
Dirty tables and chairs due to lack of proper cleaning.
No option for online food booking or pre-ordering meals.
Unavailability of meals for students attending early morning or late-night classes.
Sudden changes in menu without prior notice.Long waiting times in food service counters due to slow staff.
Mess staff giving preferential treatment to certain students.Limited number of serving spoons and cutlery, causing inconvenience.
No proper storage for student belongings while eating.
Frequent increase in mess fees without improvement in food quality.""",
    #chunk_7 data
    """ GRIEVANCES: Food portions varying from day to day without consistency.
Use of low-quality ingredients that affect taste and nutrition.
Lack of proper drainage in the dining area, leading to water accumulation.
Lack of proper seating arrangements for differently-abled students.
No clear grievance redressal mechanism for cafeteria complaints.
Unavailability of sufficient condiments like salt, pepper, and sauces.
Unhygienic water dispensers with no proper maintenance.
Lack of professional training for mess staff on hygiene and customer service.
Limited non-vegetarian meal options for students who prefer them.
Staff refusing to serve extra food even when students are willing to pay.
No separate section for students who bring their own food.
No air circulation, making the cafeteria feel suffocating.
Frequent instances of finding hair, plastic, or insects in food.
No provision for students to report spoiled food in real time.
Unavailability of affordable snacks for students between meal hours.
""",
#CHUNK8 data
""" GRIEVANCES: No flexibility for students who skip meals due to academic commitments.
No provision for students to check the menu in advance online.
No proper signage indicating where to collect food, return plates, or sit.
Excessively loud environment making it difficult to have conversations.
No option to customize meals (e.g., less spice, more protein).
No incentives for students who clean their plates to reduce food waste.
No proper response from management when complaints are raised.
Lack of nutritious, high-protein meal options for athletes and sports students.
No proper packaging for takeaway meals, causing spills and mess.
Poor time management in serving meals, causing students to miss their schedule.
Mess staff being careless while serving, leading to food spills on trays.
No separate meal counters for different food preferences (e.g., veg/non-veg).
No provision for students who have medical conditions requiring a special diet.
Lack of variety in rice or bread options (only one type served daily).
No system for pre-booking special meals on request.
Poor placement of garbage bins, leading to mess in dining areas.
No proper feedback system for students to suggest menu improvements.
Limited bakery items or desserts for students who prefer them.
Staff using excessive plastic packaging instead of eco-friendly alternatives.""",

#chunk9 data
"""GRIEVANCES:No comfortable seating arrangements for students who want to sit longer.
No provision for students to bring external food and eat in the cafeteria.
Lack of student involvement in cafeteria decision-making and food selection.
Food served is often too cold or not properly cooked.
No provision for reheating food for students who arrive late.
No proper disposal bins for biodegradable and non-biodegradable waste.
Mess staff ignoring students’ concerns about food quality.
Inconsistent meal portions given to different students.
No emergency contact number for cafeteria-related complaints.
Expired food products occasionally used in meal preparation.
No proper food handling practices leading to cross-contamination.
Lack of separate food counters for hostel and day scholars.
No discounts for students who eat fewer meals in a month.
Mess charges being deducted even when students are on leave.
No proper system for food delivery to sick students in hostels.
Unavailability of simple home-style food options for students who prefer it.
No clarity on how mess funds are used for food procurement.
Mess staff serving food without wearing gloves or aprons.
No digital payment options for students to pay for extra meals.
No flexibility in meal plans for students with varying schedules.
Lack of a designated area for faculty and staff in the cafeteria.
No CCTV cameras in the mess area to ensure hygiene and discipline.
Lack of proper seating arrangements for group discussions or study breaks.""",

#chunk 10 data
"""GRIEVANCES:Limited beverage options like tea, coffee, or milk-based drinks.
No fixed menu rotation, making meal planning unpredictable.
Delayed food preparation leading to long queues and waiting times.
No separate section for students who prefer quiet dining.
No proper lighting in the cafeteria, making it feel dull and uninviting.
Some dishes running out before all students have been served.
Poor maintenance of kitchen equipment leading to breakdowns.
No option to order smaller meal portions for students with low appetite.
Insufficient trained staff to handle large crowds efficiently.
Lack of student representatives in mess committee meetings.
Mess staff not properly trained to handle customer service issues.
Unhygienic wash areas leading to spread of germs.
Limited seasonal fruits or fresh vegetables included in meals.
No proper signage about allergens in food items.
Staff refusing to replace food when students report quality issues.
No availability of fresh yogurt, curd, or dairy-based options.
Repetitive use of deep-fried food items instead of healthy options.
Poor drainage leading to standing water and mosquito breeding.""",

#chunk 11 data
"""GRIEVANCES: Inconsistent pricing of extra food items without proper transparency.
No option for students to bring their own meal containers for takeaway.
No provision of cut fruits or salads as part of regular meals.
No regular fumigation or pest control measures in the cafeteria.
No dedicated staff to supervise and ensure cleanliness during peak hours.
No proper response mechanism for food-related health issues like stomach infections.
Inconsistent taste of the same dishes on different days.
Lack of proper hand sanitization stations at the cafeteria entrance.
No separate serving counters for students with dietary restrictions.
Mess food being wasted due to poor portion control.
No availability of fresh fruit juices or healthy drinks.
Limited breakfast options leading to students skipping meals.
No provision for light meals or snacks between major meals.
Frequent reuse of leftover food without proper storage.
No feedback mechanism for students to suggest new menu items.
Mess staff sometimes serving food with bare hands.
No system to pre-book meals for students with a busy schedule.
No proper ventilation causing food smells to linger in the dining area.
Frequent shortage of essentials like plates, spoons, and glasses.""",

#chunk12 data
"""GRIEVANCES: No fixed schedule for pest control in dining and kitchen areas.
No seasonal variety in the menu, leading to monotony.
Mess bills not being itemized, making it unclear what students are paying for.
Poor waste management leading to an unhygienic dining environment.
No provision for students to provide weekly meal preferences.
No reserved seating for students who need quick meals between classes.
No transparent mechanism for addressing food poisoning incidents.
Inadequate hot water supply for washing utensils properly.
No separate meal options for fasting students during religious observances.
Frequent delays in food preparation during special occasions.
No designated food complaint officer for immediate resolution.
Unavailability of low-calorie food options for students maintaining diets.
Frequent unavailability of essential food items like milk or curd.
No proper system for rotating and updating mess staff to maintain service quality.
Excessive salt and spices in food without a low-sodium option.
No system to track food expiry dates to ensure freshness.
Lack of proper fire safety measures in the kitchen area.
No designated meal timing for students with evening shifts.
Food ingredients sometimes having a stale or bitter taste.
""",

#chunk13 data
"""GRIEVANCES: No option for students to request half portions to reduce wastage.
Dirty tablecloths and chairs due to improper maintenance.
No information displayed about the nutritional content of meals.
No designated area for composting organic food waste.
No proper cleaning schedule for mess floors and serving areas.
Lack of food allergy awareness among mess staff.
Some food items running out before students in later batches get served.
No strict hygiene inspections conducted by health officials.
No provision for students to carry their own drinking water bottles.
Some students taking more food than needed, leading to wastage.
Mess staff sometimes ignoring hygiene practices during peak rush hours.
No availability of dietitian-approved meal plans for students’ health need.
No microwave facility for students to heat their own food.
No proper dining etiquette training for mess staff.
Some students hoarding food, leading to shortages for others.
No provision for diabetic or health-conscious students.
No arrangements for fresh bakery products like bread and rolls.
Mess staff being inattentive or slow in refilling empty food trays."""
#chunk14 data
"""Some students cutting queues, leading to unfair delays for others.
No timely supply of essential condiments like salt and sugar.
No proper process for students to cancel meals when they won’t be dining.
No provision for students to take food to-go for night study sessions.
Mess staff using excessive force while handling student complaints.
No regular audits for mess hygiene and food safety compliance.
No provision for students to give feedback on food quality.
High charges for extra food servings.
Spoiled or expired food products being used in cooking.
No provision for students to opt out of the mess and get a refund.
No proper billing system, leading to overcharging at times.
No canteen facility during academic breaks or semester vacations.
Cold food being served due to lack of proper heating equipment.
Limited drink options beyond water (e.g., fresh juice, tea, coffee).
No security or monitoring in cafeteria to prevent food theft or misuse.
No cafeteria loyalty programs or meal discount options for regular users.""",
]

department_id = "Cafeteria Department"

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
