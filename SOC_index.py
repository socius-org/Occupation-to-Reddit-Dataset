soc_index = {
    11: "Management", 
    13: "Business and Financial Operations", 
    15: "Computer and Mathematical", 
    17: "Architecture and Engineering", 
    19: "Life, Physical, and Social Science", 
    21: "Community and Social Service", 
    23: "Legal", 
    25: "Educational Instruction and Library", 
    27: "Arts, Design, Entertainment, Sports, and Media", 
    29: "Healthcare Practitioners and Technical", 
    31: "Healthcare Support", 
    33: "Protective Service", 
    35: "Food Preparation and Serving Related", 
    37: "Building and Grounds Cleaning and Maintenance", 
    39: "Personal Care and Service", 
    41: "Sales and Related", 
    43: "Office and Administrative Support", 
    45: "Farming, Fishing, and Forestry", 
    47: "Construction and Extraction", 
    49: "Installation, Maintenance, and Repair", 
    51: "Production", 
    53: "Transportation and Material Moving", 
    55: "Military Specific"
}

soc_hierarchy_index = {
    11: {# Management
        1000: "Top Executives",
        2000: "Advertising, Marketing, Promotions, Public Relations, and Sales Managers", 
        3000: "Operations Specialties Managers", 
        9000: "Other Management Occupations"
    }, 
    13: {# Business and Financial Operations
        1000: "Business Operations Specialists",
        2000: "Financial Specialists"
    }, 
    15: {# Computer and Mathematical
        1000: "Computer Occupations",
        2000: "Mathematical Science Occupations"
    }, 
    17: {# Architecture and Engineering
        1000: "Architects, Surveyors, and Cartographers",
        2000: "Engineers", 
        3000: "Drafters, Engineering Technicians, and Mapping Technicians", 
    }, 
    19: {# Life, Physical, and Social Science
        1000: "Life Scientists",
        2000: "Physical Scientists", 
        3000: "Social Scientists and Related Workers", 
        4000: "Life, Physical, and Social Science Technicians", 
        5000: "Occupational Health and Safety Specialists and Technicians"
    }, 
    21: {# Community and Social Service
        1000: "Counselors, Social Workers, and Other Community and Social Service Specialists",
        2000: "Religious Workers" 
    }, 
    23: {# Legal
        1000: "Lawyers, Judges, and Related Workers",
        2000: "Legal Support Workers"
    }, 
    25: {# Educational Instruction and Library
        1000: "Postsecondary Teachers",
        2000: "Preschool, Elementary, Middle, Secondary, and Special Education Teachers", 
        3000: "Other Teachers and Instructors", 
        4000: "Librarians, Curators, and Archivists", 
        9000: "Other Educational Instruction and Library Occupations"
    }, 
    27: {# Arts, Design, Entertainment, Sports, and Media
        1000: "Art and Design Workers",
        2000: "Entertainers and Performers, Sports and Related Workers", 
        3000: "Media and Communication Workers", 
        4000: "Media and Communication Equipment Workers"
    }, 
    29: {# Healthcare Practitioners and Technical
        1000: "Healthcare Diagnosing or Treating Practitioners",
        2000: "Health Technologists and Technicians", 
        9000: "Other Healthcare Practitioners and Technical Occupations"
    }, 
    31: {# Healthcare Support
        1000: "Home Health and Personal Care Aides; and Nursing Assistants, Orderlies, and Psychiatric Aides",
        2000: "Occupational Therapy and Physical Therapist Assistants and Aides", 
        9000: "Other Healthcare Support Occupations"
    },  
    33: {# Protective Service
        1000: "Supervisors of Protective Service Workers",
        2000: "Firefighting and Prevention Workers", 
        3000: "Law Enforcement Workers", 
        9000: "Other Protective Service Workers"
    },   
    35: {# Food Preparation and Serving Related
        1000: "Supervisors of Food Preparation and Serving Workers",
        2000: "Cooks and Food Preparation Workers", 
        3000: "Food and Beverage Serving Workers", 
        9000: "Other Food Preparation and Serving Related Workers"
    },  
    37: {# Building and Grounds Cleaning and Maintenance
        1000: "Supervisors of Building and Grounds Cleaning and Maintenance Workers",
        2000: "Building Cleaning and Pest Control Workers", 
        3000: "Grounds Maintenance Workers"
    }, 
    39: {# Personal Care and Service
        1000: "Supervisors of Personal Care and Service Workers",
        2000: "Animal Care and Service Workers", 
        3000: "Entertainment Attendants and Related Workers", 
        4000: "Funeral Service Workers", 
        5000: "Personal Appearance Workers",
        6000: "Baggage Porters, Bellhops, and Concierges", 
        7000: "Tour and Travel Guides",
        9000: "Other Personal Care and Service Workers"
    },  
    41: {# Sales and Related
        1000: "Supervisors of Sales Workers",
        2000: "Retail Sales Workers", 
        3000: "Sales Representatives, Services", 
        4000: "Sales Representatives, Wholesale and Manufacturing", 
        9000: "Other Sales and Related Workers"
    },  
    43: {# Office and Administrative Support
        1000: "Supervisors of Office and Administrative Support Workers",
        2000: "Communications Equipment Operators", 
        3000: "Financial Clerks", 
        4000: "Information and Record Clerks",
        5000: "Material Recording, Scheduling, Dispatching, and Distributing Workers", 
        6000: "Secretaries and Administrative Assistants", 
        9000: "Other Office and Administrative Support Workers"
    },  
    45: {# Farming, Fishing, and Forestry
        1000: "Supervisors of Farming, Fishing, and Forestry Workers",
        2000: "Agricultural Workers", 
        3000: "Fishing and Hunting Workers", 
        4000: "Forest, Conservation, and Logging Workers"
    },  
    47: {# Construction and Extraction
        1000: "Supervisors of Construction and Extraction Workers",
        2000: "Construction Trades Workers", 
        3000: "Helpers, Construction Trades", 
        4000: "Other Construction and Related Workers", 
        5000: "Extraction Workers"
    },  
    49: {# Installation, Maintenance, and Repair
        1000: "Supervisors of Installation, Maintenance, and Repair Workers",
        2000: "Electrical and Electronic Equipment Mechanics, Installers, and Repairers", 
        3000: "Vehicle and Mobile Equipment Mechanics, Installers, and Repairers", 
        9000: "Other Installation, Maintenance, and Repair Occupations", 
    },   
    51: {# Production
        1000: "Supervisors of Production Workers",
        2000: "Assemblers and Fabricators", 
        3000: "Food Processing Workers", 
        4000: "Metal Workers and Plastic Workers", 
        5000: "Printing Workers", 
        6000: "Textile, Apparel, and Furnishings Workers",
        7000: "Woodworkers", 
        8000: "Plant and System Operators", 
        9000: "Other Production Occupations"
    },  
    53: {# Transportation and Material Moving
        1000: "Supervisors of Transportation and Material Moving Workers",
        2000: "Air Transportation Workers", 
        3000: "Motor Vehicle Operators", 
        4000: "Rail Transportation Workers",
        5000: "Water Transportation Workers", 
        6000: "Other Transportation Workers", 
        7000: "Material Moving Workers"
    },  
    # 55: {# Military Specific
    # },  
}