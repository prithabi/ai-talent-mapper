"""
AI Talent Mapper
Intelligence Code Framework

Vidhishastra Foundation
"""

TALENT_CODES = {

    "EI2": {
        "name": "Explorer Intelligence",
        "hindi_name": "खोजकर्ता बुद्धिमत्ता",
        "description": "Natural curiosity, independent learning, experimentation and discovery.",
        "strengths": [
            "Curiosity",
            "Independent Learning",
            "Experimentation",
            "Research",
            "Problem Discovery"
        ],
        "career_paths": [
            "Scientist",
            "Researcher",
            "Data Analyst",
            "Engineer",
            "Innovation Specialist"
        ]
    },

    "9HY": {
        "name": "Agile Dynamo",
        "hindi_name": "गतिज बुद्धिमत्ता",
        "description": "Action-oriented, adaptive and hands-on problem solving.",
        "strengths": [
            "Adaptability",
            "Action",
            "Hands-on Learning",
            "Execution",
            "Physical Coordination"
        ],
        "career_paths": [
            "Sports Professional",
            "Field Engineer",
            "Technician",
            "Operations Specialist",
            "Emergency Response"
        ]
    },

    "80L": {
        "name": "Visual Architect",
        "hindi_name": "दृश्य-स्थानिक बुद्धिमत्ता",
        "description": "Visual thinking, design, spatial reasoning and creative expression.",
        "strengths": [
            "Visual Thinking",
            "Creativity",
            "Design",
            "Spatial Reasoning",
            "Imagination"
        ],
        "career_paths": [
            "Architect",
            "Designer",
            "Animator",
            "Artist",
            "UI/UX Designer"
        ]
    },

    "021": {
        "name": "Articulate Orator",
        "hindi_name": "सामाजिक-भाषाई बुद्धिमत्ता",
        "description": "Communication, leadership, empathy and language-based influence.",
        "strengths": [
            "Communication",
            "Leadership",
            "Empathy",
            "Public Speaking",
            "Team Interaction"
        ],
        "career_paths": [
            "Teacher",
            "Leader",
            "Counselor",
            "Content Creator",
            "Public Speaker"
        ]
    },

    "23BR": {
        "name": "Efficiency Expert",
        "hindi_name": "तार्किक-विश्लेषणात्मक बुद्धिमत्ता",
        "description": "Logical reasoning, data analysis, systems thinking and efficiency.",
        "strengths": [
            "Logical Thinking",
            "Data Analysis",
            "Mathematics",
            "Systems Thinking",
            "Optimization"
        ],
        "career_paths": [
            "Data Scientist",
            "Business Analyst",
            "Software Engineer",
            "AI/ML Engineer",
            "Financial Analyst"
        ]
    },

    "D1": {
        "name": "Self-Reliant Maverick",
        "hindi_name": "स्व-निर्भर बुद्धिमत्ता",
        "description": "Strong autonomy, self-direction and independent decision making.",
        "strengths": [
            "Independence",
            "Self Direction",
            "Decision Making",
            "Initiative",
            "Responsibility"
        ],
        "career_paths": [
            "Entrepreneur",
            "Founder",
            "Independent Consultant",
            "Project Leader",
            "Creative Professional"
        ]
    }
}


def get_talent_code(code):
    """
    Return information for a specific Intelligence Code.
    """
    return TALENT_CODES.get(code)


def get_all_talent_codes():
    """
    Return all Intelligence Codes.
    """
    return TALENT_CODES
