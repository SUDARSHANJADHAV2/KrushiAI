"""
Comprehensive Plant Disease Information Database
Contains detailed information about symptoms, treatments, and prevention methods
for all 38 plant diseases in the model.
"""

DISEASE_INFO = {
    "Apple___Apple_scab": {
        "name": "Apple Scab",
        "plant": "Apple",
        "scientific_name": "Venturia inaequalis",
        "severity": "High",
        "description": "A fungal disease that causes dark, scabby lesions on leaves, fruit, and twigs.",
        "symptoms": [
            "Dark, olive-green to black spots on leaves",
            "Scabby lesions on fruit surface",
            "Premature leaf drop",
            "Reduced fruit quality and yield"
        ],
        "causes": [
            "Fungal pathogen Venturia inaequalis",
            "Wet, humid weather conditions",
            "Poor air circulation",
            "Infected plant debris"
        ],
        "treatment": [
            "Apply fungicide sprays during wet periods",
            "Remove infected leaves and debris",
            "Improve air circulation through pruning",
            "Use resistant apple varieties"
        ],
        "prevention": [
            "Plant disease-resistant varieties",
            "Ensure good air circulation",
            "Clean up fallen leaves in autumn",
            "Apply preventive fungicide treatments"
        ]
    },
    "Apple___Black_rot": {
        "name": "Apple Black Rot",
        "plant": "Apple",
        "scientific_name": "Botryosphaeria obtusa",
        "severity": "High",
        "description": "A serious fungal disease causing fruit rot and cankers on branches.",
        "symptoms": [
            "Black, circular lesions on fruit",
            "Brown leaf spots with purple margins",
            "Cankers on branches and trunk",
            "Fruit mummification"
        ],
        "causes": [
            "Fungal pathogen Botryosphaeria obtusa",
            "Stress conditions on trees",
            "Wounds and injuries",
            "Wet weather conditions"
        ],
        "treatment": [
            "Remove infected fruit and branches",
            "Apply copper-based fungicides",
            "Prune to improve air circulation",
            "Maintain tree vigor"
        ],
        "prevention": [
            "Proper pruning and sanitation",
            "Avoid tree stress",
            "Regular inspection and early detection",
            "Apply preventive fungicide sprays"
        ]
    },
    "Apple___Cedar_apple_rust": {
        "name": "Cedar Apple Rust",
        "plant": "Apple",
        "scientific_name": "Gymnosporangium juniperi-virginianae",
        "severity": "Medium",
        "description": "A fungal disease that alternates between apple and cedar trees.",
        "symptoms": [
            "Yellow-orange spots on upper leaf surface",
            "Orange, cup-shaped structures under leaves",
            "Premature defoliation",
            "Reduced fruit quality"
        ],
        "causes": [
            "Fungal pathogen requiring both apple and cedar hosts",
            "Wet spring weather",
            "Proximity to cedar trees",
            "Wind-dispersed spores"
        ],
        "treatment": [
            "Apply fungicide during spring",
            "Remove nearby cedar trees if possible",
            "Improve air circulation",
            "Clean up infected debris"
        ],
        "prevention": [
            "Plant resistant apple varieties",
            "Remove alternate cedar hosts",
            "Apply preventive fungicide treatments",
            "Maintain proper tree spacing"
        ]
    },
    "Apple___healthy": {
        "name": "Healthy Apple",
        "plant": "Apple",
        "scientific_name": "Malus domestica",
        "severity": "None",
        "description": "Healthy apple plant showing normal growth and development.",
        "symptoms": [
            "Green, vigorous foliage",
            "No visible disease symptoms",
            "Normal fruit development",
            "Good overall plant health"
        ],
        "causes": ["Normal, healthy plant growth"],
        "treatment": ["No treatment needed - maintain current care"],
        "prevention": [
            "Continue regular monitoring",
            "Maintain proper watering and nutrition",
            "Practice good sanitation",
            "Regular pruning for air circulation"
        ]
    },
    "Blueberry___healthy": {
        "name": "Healthy Blueberry",
        "plant": "Blueberry",
        "scientific_name": "Vaccinium corymbosum",
        "severity": "None",
        "description": "Healthy blueberry plant with normal growth patterns.",
        "symptoms": [
            "Dark green, healthy leaves",
            "Normal berry development",
            "Good plant vigor",
            "No disease symptoms"
        ],
        "causes": ["Normal, healthy plant growth"],
        "treatment": ["No treatment needed - maintain current care"],
        "prevention": [
            "Maintain acidic soil conditions",
            "Ensure proper drainage",
            "Regular monitoring for pests and diseases",
            "Appropriate fertilization"
        ]
    },
    "Cherry_(including_sour)___Powdery_mildew": {
        "name": "Cherry Powdery Mildew",
        "plant": "Cherry",
        "scientific_name": "Podosphaera clandestina",
        "severity": "Medium",
        "description": "Fungal disease causing white powdery growth on leaves and shoots.",
        "symptoms": [
            "White powdery coating on leaves",
            "Leaf curling and distortion",
            "Stunted shoot growth",
            "Reduced fruit quality"
        ],
        "causes": [
            "Fungal pathogen Podosphaera clandestina",
            "Humid conditions with moderate temperatures",
            "Poor air circulation",
            "Dense plant growth"
        ],
        "treatment": [
            "Apply fungicide treatments",
            "Remove infected plant parts",
            "Improve air circulation",
            "Reduce humidity around plants"
        ],
        "prevention": [
            "Plant in well-ventilated areas",
            "Avoid overhead watering",
            "Regular pruning for air circulation",
            "Apply preventive fungicide sprays"
        ]
    },
    "Cherry_(including_sour)___healthy": {
        "name": "Healthy Cherry",
        "plant": "Cherry",
        "scientific_name": "Prunus species",
        "severity": "None",
        "description": "Healthy cherry tree showing normal growth and fruit development.",
        "symptoms": [
            "Vibrant green foliage",
            "Normal fruit development",
            "Good tree structure",
            "No visible disease symptoms"
        ],
        "causes": ["Normal, healthy plant growth"],
        "treatment": ["No treatment needed - maintain current care"],
        "prevention": [
            "Regular pruning and maintenance",
            "Proper watering and fertilization",
            "Monitor for pest and disease issues",
            "Maintain good soil drainage"
        ]
    },
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot": {
        "name": "Corn Gray Leaf Spot",
        "plant": "Corn/Maize",
        "scientific_name": "Cercospora zeae-maydis",
        "severity": "High",
        "description": "Fungal disease causing rectangular gray lesions on corn leaves.",
        "symptoms": [
            "Rectangular gray-brown lesions on leaves",
            "Lesions parallel to leaf veins",
            "Premature leaf death",
            "Reduced photosynthesis and yield"
        ],
        "causes": [
            "Fungal pathogen Cercospora zeae-maydis",
            "High humidity and warm temperatures",
            "Extended leaf wetness periods",
            "Dense plant populations"
        ],
        "treatment": [
            "Apply fungicide treatments",
            "Remove infected plant debris",
            "Improve air circulation",
            "Rotate crops"
        ],
        "prevention": [
            "Plant resistant corn varieties",
            "Crop rotation with non-host crops",
            "Reduce plant density",
            "Remove crop residue after harvest"
        ]
    },
    "Corn_(maize)___Common_rust_": {
        "name": "Corn Common Rust",
        "plant": "Corn/Maize",
        "scientific_name": "Puccinia sorghi",
        "severity": "Medium",
        "description": "Fungal rust disease forming orange-brown pustules on corn leaves.",
        "symptoms": [
            "Small orange-brown pustules on leaves",
            "Pustules on both leaf surfaces",
            "Yellowing and premature leaf death",
            "Reduced plant vigor"
        ],
        "causes": [
            "Fungal pathogen Puccinia sorghi",
            "Cool, moist weather conditions",
            "Wind-dispersed spores",
            "Alternate host plants nearby"
        ],
        "treatment": [
            "Apply fungicide if severe",
            "Remove alternate host weeds",
            "Monitor weather conditions",
            "Maintain plant nutrition"
        ],
        "prevention": [
            "Plant resistant corn hybrids",
            "Control alternate host weeds",
            "Monitor for early symptoms",
            "Maintain balanced nutrition"
        ]
    },
    "Corn_(maize)___Northern_Leaf_Blight": {
        "name": "Northern Corn Leaf Blight",
        "plant": "Corn/Maize",
        "scientific_name": "Setosphaeria turcica",
        "severity": "High",
        "description": "Fungal disease causing large, cigar-shaped lesions on corn leaves.",
        "symptoms": [
            "Large, cigar-shaped gray-green lesions",
            "Lesions become tan with dark borders",
            "Lesions may cover entire leaf",
            "Significant yield reduction possible"
        ],
        "causes": [
            "Fungal pathogen Setosphaeria turcica",
            "Moderate temperatures and high humidity",
            "Extended periods of leaf wetness",
            "Infected crop debris"
        ],
        "treatment": [
            "Apply fungicide treatments",
            "Remove infected plant material",
            "Improve air circulation",
            "Crop rotation"
        ],
        "prevention": [
            "Plant resistant corn varieties",
            "Tillage to bury crop residue",
            "Crop rotation with non-host crops",
            "Balanced fertilization"
        ]
    },
    "Corn_(maize)___healthy": {
        "name": "Healthy Corn",
        "plant": "Corn/Maize",
        "scientific_name": "Zea mays",
        "severity": "None",
        "description": "Healthy corn plant with normal growth and ear development.",
        "symptoms": [
            "Dark green, healthy leaves",
            "Normal ear development",
            "Good plant height and structure",
            "No disease symptoms visible"
        ],
        "causes": ["Normal, healthy plant growth"],
        "treatment": ["No treatment needed - maintain current care"],
        "prevention": [
            "Maintain proper nutrition",
            "Ensure adequate water supply",
            "Monitor for pest and disease issues",
            "Practice crop rotation"
        ]
    },
    "Grape___Black_rot": {
        "name": "Grape Black Rot",
        "plant": "Grape",
        "scientific_name": "Guignardia bidwellii",
        "severity": "High",
        "description": "Serious fungal disease affecting grape leaves, shoots, and fruit.",
        "symptoms": [
            "Circular brown leaf spots",
            "Black, mummified berries",
            "Brown lesions on shoots",
            "Severe fruit loss"
        ],
        "causes": [
            "Fungal pathogen Guignardia bidwellii",
            "Warm, wet weather conditions",
            "Poor air circulation",
            "Infected plant debris"
        ],
        "treatment": [
            "Apply fungicide treatments",
            "Remove infected fruit and leaves",
            "Prune for better air circulation",
            "Sanitation practices"
        ],
        "prevention": [
            "Plant resistant grape varieties",
            "Ensure good air circulation",
            "Remove infected debris",
            "Apply preventive fungicide sprays"
        ]
    },
    "Grape___Esca_(Black_Measles)": {
        "name": "Grape Esca (Black Measles)",
        "plant": "Grape",
        "scientific_name": "Multiple fungal pathogens",
        "severity": "High",
        "description": "Complex fungal disease causing wood decay and leaf symptoms.",
        "symptoms": [
            "Interveinal chlorosis and necrosis",
            "Tiger stripe pattern on leaves",
            "Black spots on berries",
            "Wood decay in trunk and arms"
        ],
        "causes": [
            "Complex of fungal pathogens",
            "Pruning wounds and injuries",
            "Stress conditions",
            "Age of the vine"
        ],
        "treatment": [
            "Remove infected wood",
            "Protect pruning wounds",
            "Improve vine nutrition",
            "Consider trunk renewal"
        ],
        "prevention": [
            "Proper pruning techniques",
            "Wound protection",
            "Stress reduction",
            "Regular vine monitoring"
        ]
    },
    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)": {
        "name": "Grape Leaf Blight",
        "plant": "Grape",
        "scientific_name": "Isariopsis leaf spot",
        "severity": "Medium",
        "description": "Fungal disease causing leaf spots and blight symptoms.",
        "symptoms": [
            "Dark brown to black leaf spots",
            "Irregular lesion shapes",
            "Premature defoliation",
            "Reduced vine vigor"
        ],
        "causes": [
            "Fungal pathogen",
            "High humidity and moisture",
            "Poor air circulation",
            "Dense canopy growth"
        ],
        "treatment": [
            "Apply appropriate fungicides",
            "Remove infected leaves",
            "Improve air circulation",
            "Reduce humidity levels"
        ],
        "prevention": [
            "Proper vine spacing",
            "Regular pruning for air flow",
            "Avoid overhead irrigation",
            "Monitor humidity levels"
        ]
    },
    "Grape___healthy": {
        "name": "Healthy Grape",
        "plant": "Grape",
        "scientific_name": "Vitis vinifera",
        "severity": "None",
        "description": "Healthy grapevine with normal leaf and fruit development.",
        "symptoms": [
            "Green, vigorous foliage",
            "Normal berry development",
            "Good vine structure",
            "No visible disease symptoms"
        ],
        "causes": ["Normal, healthy plant growth"],
        "treatment": ["No treatment needed - maintain current care"],
        "prevention": [
            "Regular pruning and training",
            "Proper nutrition management",
            "Monitor for disease and pests",
            "Maintain good air circulation"
        ]
    },
    "Orange___Haunglongbing_(Citrus_greening)": {
        "name": "Citrus Greening (HLB)",
        "plant": "Orange/Citrus",
        "scientific_name": "Candidatus Liberibacter asiaticus",
        "severity": "Critical",
        "description": "Devastating bacterial disease spread by Asian citrus psyllid.",
        "symptoms": [
            "Yellow shoots and mottled leaves",
            "Asymmetrical leaf yellowing",
            "Small, bitter, misshapen fruit",
            "Tree decline and death"
        ],
        "causes": [
            "Bacterial pathogen Candidatus Liberibacter",
            "Spread by Asian citrus psyllid",
            "No cure available",
            "Systemic infection"
        ],
        "treatment": [
            "Remove infected trees immediately",
            "Control psyllid vectors",
            "No effective treatment available",
            "Focus on prevention"
        ],
        "prevention": [
            "Control Asian citrus psyllid",
            "Plant certified disease-free trees",
            "Early detection and removal",
            "Area-wide management programs"
        ]
    },
    "Peach___Bacterial_spot": {
        "name": "Peach Bacterial Spot",
        "plant": "Peach",
        "scientific_name": "Xanthomonas arboricola pv. pruni",
        "severity": "High",
        "description": "Bacterial disease affecting leaves, twigs, and fruit of stone fruits.",
        "symptoms": [
            "Small, dark spots on leaves",
            "Shot-hole appearance in leaves",
            "Sunken lesions on fruit",
            "Twig cankers and dieback"
        ],
        "causes": [
            "Bacterial pathogen Xanthomonas arboricola",
            "Warm, wet weather conditions",
            "Overhead irrigation",
            "Infected plant material"
        ],
        "treatment": [
            "Apply copper-based bactericides",
            "Remove infected plant parts",
            "Improve air circulation",
            "Avoid overhead watering"
        ],
        "prevention": [
            "Plant resistant varieties",
            "Avoid overhead irrigation",
            "Proper pruning for air flow",
            "Copper sprays during dormancy"
        ]
    },
    "Peach___healthy": {
        "name": "Healthy Peach",
        "plant": "Peach",
        "scientific_name": "Prunus persica",
        "severity": "None",
        "description": "Healthy peach tree with normal growth and fruit development.",
        "symptoms": [
            "Healthy green foliage",
            "Normal fruit development",
            "Good tree structure",
            "No disease symptoms"
        ],
        "causes": ["Normal, healthy plant growth"],
        "treatment": ["No treatment needed - maintain current care"],
        "prevention": [
            "Regular pruning and maintenance",
            "Proper irrigation management",
            "Monitor for disease and pests",
            "Maintain tree nutrition"
        ]
    },
    "Pepper,_bell___Bacterial_spot": {
        "name": "Pepper Bacterial Spot",
        "plant": "Bell Pepper",
        "scientific_name": "Xanthomonas campestris pv. vesicatoria",
        "severity": "High",
        "description": "Bacterial disease causing spots on leaves and fruit of peppers.",
        "symptoms": [
            "Small, dark spots on leaves",
            "Yellow halos around leaf spots",
            "Scabby lesions on fruit",
            "Premature fruit drop"
        ],
        "causes": [
            "Bacterial pathogen Xanthomonas campestris",
            "Warm, humid conditions",
            "Overhead watering",
            "Contaminated seeds or transplants"
        ],
        "treatment": [
            "Apply copper-based bactericides",
            "Remove infected plants",
            "Improve air circulation",
            "Avoid working with wet plants"
        ],
        "prevention": [
            "Use disease-free seeds",
            "Avoid overhead irrigation",
            "Crop rotation",
            "Copper sprays as preventive"
        ]
    },
    "Pepper,_bell___healthy": {
        "name": "Healthy Bell Pepper",
        "plant": "Bell Pepper",
        "scientific_name": "Capsicum annuum",
        "severity": "None",
        "description": "Healthy pepper plant with normal growth and fruit production.",
        "symptoms": [
            "Dark green, healthy leaves",
            "Normal fruit development",
            "Good plant vigor",
            "No disease symptoms"
        ],
        "causes": ["Normal, healthy plant growth"],
        "treatment": ["No treatment needed - maintain current care"],
        "prevention": [
            "Maintain proper watering",
            "Ensure good nutrition",
            "Monitor for pests and diseases",
            "Practice crop rotation"
        ]
    },
    "Potato___Early_blight": {
        "name": "Potato Early Blight",
        "plant": "Potato",
        "scientific_name": "Alternaria solani",
        "severity": "High",
        "description": "Fungal disease causing leaf spots and tuber lesions in potatoes.",
        "symptoms": [
            "Brown leaf spots with concentric rings",
            "Target-like lesions on leaves",
            "Premature defoliation",
            "Dark lesions on tubers"
        ],
        "causes": [
            "Fungal pathogen Alternaria solani",
            "Warm, humid weather",
            "Plant stress and poor nutrition",
            "Extended leaf wetness"
        ],
        "treatment": [
            "Apply fungicide treatments",
            "Remove infected plant debris",
            "Improve air circulation",
            "Maintain plant nutrition"
        ],
        "prevention": [
            "Plant certified seed potatoes",
            "Crop rotation",
            "Avoid overhead irrigation",
            "Maintain proper plant nutrition"
        ]
    },
    "Potato___Late_blight": {
        "name": "Potato Late Blight",
        "plant": "Potato",
        "scientific_name": "Phytophthora infestans",
        "severity": "Critical",
        "description": "Devastating oomycete disease that caused the Irish Potato Famine.",
        "symptoms": [
            "Water-soaked lesions on leaves",
            "White fuzzy growth on leaf undersides",
            "Blackening and collapse of foliage",
            "Brown rot of tubers"
        ],
        "causes": [
            "Oomycete pathogen Phytophthora infestans",
            "Cool, wet weather conditions",
            "High humidity",
            "Wind-dispersed spores"
        ],
        "treatment": [
            "Apply fungicide immediately",
            "Remove infected plants",
            "Destroy infected tubers",
            "Improve drainage"
        ],
        "prevention": [
            "Plant certified disease-free seed",
            "Monitor weather conditions",
            "Apply preventive fungicides",
            "Ensure good air circulation"
        ]
    },
    "Potato___healthy": {
        "name": "Healthy Potato",
        "plant": "Potato",
        "scientific_name": "Solanum tuberosum",
        "severity": "None",
        "description": "Healthy potato plant with normal growth and tuber development.",
        "symptoms": [
            "Green, vigorous foliage",
            "Normal tuber development",
            "Good plant structure",
            "No disease symptoms"
        ],
        "causes": ["Normal, healthy plant growth"],
        "treatment": ["No treatment needed - maintain current care"],
        "prevention": [
            "Use certified seed potatoes",
            "Practice crop rotation",
            "Maintain proper nutrition",
            "Monitor for disease and pests"
        ]
    },
    "Raspberry___healthy": {
        "name": "Healthy Raspberry",
        "plant": "Raspberry",
        "scientific_name": "Rubus idaeus",
        "severity": "None",
        "description": "Healthy raspberry cane with normal growth and berry production.",
        "symptoms": [
            "Healthy green canes and leaves",
            "Normal berry development",
            "Good cane vigor",
            "No disease symptoms"
        ],
        "causes": ["Normal, healthy plant growth"],
        "treatment": ["No treatment needed - maintain current care"],
        "prevention": [
            "Regular cane pruning",
            "Good air circulation",
            "Monitor for disease and pests",
            "Maintain proper nutrition"
        ]
    },
    "Soybean___healthy": {
        "name": "Healthy Soybean",
        "plant": "Soybean",
        "scientific_name": "Glycine max",
        "severity": "None",
        "description": "Healthy soybean plant with normal growth and pod development.",
        "symptoms": [
            "Green, healthy foliage",
            "Normal pod development",
            "Good plant structure",
            "No disease symptoms"
        ],
        "causes": ["Normal, healthy plant growth"],
        "treatment": ["No treatment needed - maintain current care"],
        "prevention": [
            "Practice crop rotation",
            "Monitor for disease and pests",
            "Maintain proper nutrition",
            "Use certified seeds"
        ]
    },
    "Squash___Powdery_mildew": {
        "name": "Squash Powdery Mildew",
        "plant": "Squash",
        "scientific_name": "Podosphaera xanthii",
        "severity": "Medium",
        "description": "Fungal disease creating white powdery coating on squash leaves.",
        "symptoms": [
            "White powdery coating on leaves",
            "Yellowing and wilting of leaves",
            "Stunted plant growth",
            "Reduced fruit quality"
        ],
        "causes": [
            "Fungal pathogen Podosphaera xanthii",
            "Warm days and cool nights",
            "High humidity",
            "Poor air circulation"
        ],
        "treatment": [
            "Apply fungicide treatments",
            "Remove infected leaves",
            "Improve air circulation",
            "Reduce humidity"
        ],
        "prevention": [
            "Plant resistant varieties",
            "Ensure good air circulation",
            "Avoid overhead watering",
            "Regular monitoring"
        ]
    },
    "Strawberry___Leaf_scorch": {
        "name": "Strawberry Leaf Scorch",
        "plant": "Strawberry",
        "scientific_name": "Diplocarpon earlianum",
        "severity": "Medium",
        "description": "Fungal disease causing leaf scorch symptoms in strawberries.",
        "symptoms": [
            "Purple-bordered leaf spots",
            "Scorched appearance of leaves",
            "Premature leaf death",
            "Reduced plant vigor"
        ],
        "causes": [
            "Fungal pathogen Diplocarpon earlianum",
            "Wet, humid conditions",
            "Extended leaf wetness",
            "Poor air circulation"
        ],
        "treatment": [
            "Apply fungicide treatments",
            "Remove infected leaves",
            "Improve air circulation",
            "Reduce overhead watering"
        ],
        "prevention": [
            "Plant resistant varieties",
            "Ensure good drainage",
            "Avoid overhead irrigation",
            "Regular sanitation"
        ]
    },
    "Strawberry___healthy": {
        "name": "Healthy Strawberry",
        "plant": "Strawberry",
        "scientific_name": "Fragaria × ananassa",
        "severity": "None",
        "description": "Healthy strawberry plant with normal growth and fruit production.",
        "symptoms": [
            "Green, healthy leaves",
            "Normal fruit development",
            "Good plant vigor",
            "No disease symptoms"
        ],
        "causes": ["Normal, healthy plant growth"],
        "treatment": ["No treatment needed - maintain current care"],
        "prevention": [
            "Maintain proper spacing",
            "Ensure good drainage",
            "Regular monitoring",
            "Proper fertilization"
        ]
    },
    "Tomato___Bacterial_spot": {
        "name": "Tomato Bacterial Spot",
        "plant": "Tomato",
        "scientific_name": "Xanthomonas campestris pv. vesicatoria",
        "severity": "High",
        "description": "Bacterial disease causing spots on tomato leaves and fruit.",
        "symptoms": [
            "Small, dark spots on leaves",
            "Yellow halos around leaf spots",
            "Scabby lesions on fruit",
            "Defoliation and fruit drop"
        ],
        "causes": [
            "Bacterial pathogen Xanthomonas campestris",
            "Warm, humid weather",
            "Overhead watering",
            "Contaminated seeds or tools"
        ],
        "treatment": [
            "Apply copper-based bactericides",
            "Remove infected plants",
            "Improve air circulation",
            "Avoid overhead watering"
        ],
        "prevention": [
            "Use certified disease-free seeds",
            "Avoid overhead irrigation",
            "Crop rotation",
            "Sanitize tools and equipment"
        ]
    },
    "Tomato___Early_blight": {
        "name": "Tomato Early Blight",
        "plant": "Tomato",
        "scientific_name": "Alternaria solani",
        "severity": "High",
        "description": "Fungal disease causing characteristic target-like lesions on tomato plants.",
        "symptoms": [
            "Brown leaf spots with concentric rings",
            "Target-like lesions",
            "Yellowing and defoliation",
            "Fruit lesions near stem end"
        ],
        "causes": [
            "Fungal pathogen Alternaria solani",
            "Warm, humid conditions",
            "Plant stress",
            "Extended leaf wetness"
        ],
        "treatment": [
            "Apply fungicide treatments",
            "Remove infected plant parts",
            "Improve air circulation",
            "Maintain plant health"
        ],
        "prevention": [
            "Crop rotation",
            "Avoid overhead watering",
            "Mulching to reduce soil splash",
            "Proper plant spacing"
        ]
    },
    "Tomato___Late_blight": {
        "name": "Tomato Late Blight",
        "plant": "Tomato",
        "scientific_name": "Phytophthora infestans",
        "severity": "Critical",
        "description": "Devastating oomycete disease that can destroy tomato crops quickly.",
        "symptoms": [
            "Water-soaked lesions on leaves",
            "White fuzzy growth on leaf undersides",
            "Rapid blackening of foliage",
            "Brown, greasy fruit rot"
        ],
        "causes": [
            "Oomycete pathogen Phytophthora infestans",
            "Cool, wet weather",
            "High humidity",
            "Wind-dispersed spores"
        ],
        "treatment": [
            "Apply fungicide immediately",
            "Remove infected plants",
            "Improve air circulation",
            "Reduce humidity"
        ],
        "prevention": [
            "Monitor weather conditions",
            "Apply preventive fungicides",
            "Ensure good air circulation",
            "Avoid overhead irrigation"
        ]
    },
    "Tomato___Leaf_Mold": {
        "name": "Tomato Leaf Mold",
        "plant": "Tomato",
        "scientific_name": "Passalora fulva",
        "severity": "Medium",
        "description": "Fungal disease causing yellow spots and fuzzy growth on tomato leaves.",
        "symptoms": [
            "Yellow spots on upper leaf surface",
            "Fuzzy olive-green growth on undersides",
            "Leaf curling and wilting",
            "Reduced fruit quality"
        ],
        "causes": [
            "Fungal pathogen Passalora fulva",
            "High humidity in greenhouses",
            "Poor air circulation",
            "Extended periods of leaf wetness"
        ],
        "treatment": [
            "Improve ventilation",
            "Reduce humidity levels",
            "Apply appropriate fungicides",
            "Remove infected leaves"
        ],
        "prevention": [
            "Ensure good ventilation",
            "Avoid overhead watering",
            "Monitor humidity levels",
            "Plant resistant varieties"
        ]
    },
    "Tomato___Septoria_leaf_spot": {
        "name": "Tomato Septoria Leaf Spot",
        "plant": "Tomato",
        "scientific_name": "Septoria lycopersici",
        "severity": "Medium",
        "description": "Fungal disease causing small, circular spots with dark borders on tomato leaves.",
        "symptoms": [
            "Small, circular spots with dark borders",
            "White or gray centers with tiny black specks",
            "Lower leaves affected first",
            "Progressive defoliation upward"
        ],
        "causes": [
            "Fungal pathogen Septoria lycopersici",
            "Warm, wet weather",
            "High humidity",
            "Splash dispersal from soil"
        ],
        "treatment": [
            "Apply fungicide treatments",
            "Remove infected lower leaves",
            "Improve air circulation",
            "Mulch to reduce soil splash"
        ],
        "prevention": [
            "Avoid overhead watering",
            "Mulching around plants",
            "Proper plant spacing",
            "Crop rotation"
        ]
    },
    "Tomato___Spider_mites Two-spotted_spider_mite": {
        "name": "Tomato Spider Mites",
        "plant": "Tomato",
        "scientific_name": "Tetranychus urticae",
        "severity": "Medium",
        "description": "Pest damage from two-spotted spider mites causing stippling and webbing.",
        "symptoms": [
            "Fine stippling on leaves",
            "Yellow or bronze discoloration",
            "Fine webbing on plants",
            "Leaf drop in severe cases"
        ],
        "causes": [
            "Two-spotted spider mite infestation",
            "Hot, dry conditions",
            "Low humidity",
            "Dusty conditions"
        ],
        "treatment": [
            "Apply miticide treatments",
            "Increase humidity around plants",
            "Remove heavily infested leaves",
            "Use predatory mites"
        ],
        "prevention": [
            "Maintain adequate humidity",
            "Regular monitoring",
            "Avoid dusty conditions",
            "Encourage beneficial insects"
        ]
    },
    "Tomato___Target_Spot": {
        "name": "Tomato Target Spot",
        "plant": "Tomato",
        "scientific_name": "Corynespora cassiicola",
        "severity": "Medium",
        "description": "Fungal disease causing target-like spots on tomato leaves and fruit.",
        "symptoms": [
            "Brown spots with concentric rings",
            "Target-like appearance",
            "Spots on leaves, stems, and fruit",
            "Premature defoliation"
        ],
        "causes": [
            "Fungal pathogen Corynespora cassiicola",
            "Warm, humid conditions",
            "Extended leaf wetness",
            "Poor air circulation"
        ],
        "treatment": [
            "Apply fungicide treatments",
            "Remove infected plant parts",
            "Improve air circulation",
            "Reduce humidity"
        ],
        "prevention": [
            "Ensure good ventilation",
            "Avoid overhead watering",
            "Proper plant spacing",
            "Regular sanitation"
        ]
    },
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus": {
        "name": "Tomato Yellow Leaf Curl Virus",
        "plant": "Tomato",
        "scientific_name": "TYLCV",
        "severity": "Critical",
        "description": "Viral disease spread by whiteflies causing severe stunting and leaf curling.",
        "symptoms": [
            "Upward curling of leaves",
            "Yellowing of leaf margins",
            "Severe stunting of plants",
            "Reduced or no fruit production"
        ],
        "causes": [
            "Tomato Yellow Leaf Curl Virus",
            "Transmitted by whiteflies",
            "No cure available",
            "Contaminated plant material"
        ],
        "treatment": [
            "Remove infected plants immediately",
            "Control whitefly vectors",
            "No treatment available",
            "Focus on prevention"
        ],
        "prevention": [
            "Control whitefly populations",
            "Use virus-free transplants",
            "Install insect screening",
            "Plant resistant varieties"
        ]
    },
    "Tomato___Tomato_mosaic_virus": {
        "name": "Tomato Mosaic Virus",
        "plant": "Tomato",
        "scientific_name": "ToMV",
        "severity": "High",
        "description": "Viral disease causing mosaic patterns and distortion in tomato plants.",
        "symptoms": [
            "Mosaic patterns on leaves",
            "Light and dark green mottling",
            "Leaf distortion and curling",
            "Stunted growth and reduced yield"
        ],
        "causes": [
            "Tomato Mosaic Virus",
            "Mechanical transmission",
            "Contaminated tools and hands",
            "Infected plant debris"
        ],
        "treatment": [
            "Remove infected plants",
            "Sanitize tools and equipment",
            "No chemical treatment available",
            "Practice good hygiene"
        ],
        "prevention": [
            "Use certified virus-free seeds",
            "Sanitize tools regularly",
            "Avoid working with wet plants",
            "Remove infected plant debris"
        ]
    },
    "Tomato___healthy": {
        "name": "Healthy Tomato",
        "plant": "Tomato",
        "scientific_name": "Solanum lycopersicum",
        "severity": "None",
        "description": "Healthy tomato plant with normal growth and fruit development.",
        "symptoms": [
            "Green, vigorous foliage",
            "Normal fruit development",
            "Good plant structure",
            "No disease symptoms"
        ],
        "causes": ["Normal, healthy plant growth"],
        "treatment": ["No treatment needed - maintain current care"],
        "prevention": [
            "Continue proper watering",
            "Maintain good nutrition",
            "Monitor for pests and diseases",
            "Practice crop rotation"
        ]
    }
}

def get_disease_info(disease_key):
    """
    Get comprehensive information about a specific disease.
    
    Args:
        disease_key (str): The disease classification key
        
    Returns:
        dict: Disease information dictionary
    """
    return DISEASE_INFO.get(disease_key, {
        "name": "Unknown Disease",
        "description": "Disease information not available",
        "symptoms": ["Information not available"],
        "treatment": ["Consult with agricultural expert"],
        "prevention": ["Regular monitoring recommended"]
    })

def get_all_diseases():
    """Get list of all diseases in the database."""
    return list(DISEASE_INFO.keys())

def get_diseases_by_plant(plant_name):
    """Get all diseases for a specific plant type."""
    plant_diseases = []
    for disease_key, info in DISEASE_INFO.items():
        if plant_name.lower() in info.get('plant', '').lower():
            plant_diseases.append(disease_key)
    return plant_diseases

def get_severity_stats():
    """Get statistics about disease severity levels."""
    severity_counts = {}
    for info in DISEASE_INFO.values():
        severity = info.get('severity', 'Unknown')
        severity_counts[severity] = severity_counts.get(severity, 0) + 1
    return severity_counts