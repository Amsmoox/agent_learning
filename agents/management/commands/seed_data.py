from django.core.management.base import BaseCommand
import json
from agents.models import Student, Quiz
import random

class Command(BaseCommand):
    help = 'Seeds the database with demo data'

    def handle(self, *args, **kwargs):
        # Create 10 demo students
        student_names = [
            "Emma Thompson", "James Chen", "Sofia Rodriguez", "Alex Kim",
            "Maya Patel", "Lucas Weber", "Olivia Brown", "Ethan Davis",
            "Ava Wilson", "Noah Garcia"
        ]

        traits_templates = [
            {"confidence": 0.7, "attention_span": 0.8, "learning_style": "visual"},
            {"confidence": 0.5, "attention_span": 0.9, "learning_style": "auditory"},
            {"confidence": 0.9, "attention_span": 0.6, "learning_style": "kinesthetic"},
            {"confidence": 0.6, "attention_span": 0.7, "learning_style": "reading/writing"}
        ]

        self.stdout.write('Creating demo students...')
        for name in student_names:
            traits = random.choice(traits_templates)
            traits["adaptability"] = round(random.uniform(0.4, 0.9), 2)
            
            Student.objects.create(
                name=name,
                baseline_understanding_pct=round(random.uniform(60, 95), 2),
                traits_json=traits
            )

        # Create demo quiz
        self.stdout.write('Creating demo quiz...')
        demo_quiz = {
            "title": "Introduction to AI Concepts",
            "questions": [
                {
                    "id": 1,
                    "question": "What is machine learning?",
                    "options": [
                        "A type of computer hardware",
                        "The ability of systems to learn from data",
                        "A programming language",
                        "A database management system"
                    ],
                    "correct_answer": 1
                },
                {
                    "id": 2,
                    "question": "What is supervised learning?",
                    "options": [
                        "Learning without a teacher",
                        "Learning with labeled data",
                        "Learning through reinforcement",
                        "Learning through observation"
                    ],
                    "correct_answer": 1
                },
                {
                    "id": 3,
                    "question": "What is deep learning?",
                    "options": [
                        "Learning while sleeping",
                        "Learning using neural networks with many layers",
                        "Learning from books",
                        "Learning through meditation"
                    ],
                    "correct_answer": 1
                },
                {
                    "id": 4,
                    "question": "What is natural language processing?",
                    "options": [
                        "Processing organic food",
                        "Understanding and generating human language",
                        "Processing raw materials",
                        "Processing binary code"
                    ],
                    "correct_answer": 1
                },
                {
                    "id": 5,
                    "question": "What is reinforcement learning?",
                    "options": [
                        "Learning through punishment",
                        "Learning through rewards and penalties",
                        "Learning through repetition",
                        "Learning through observation"
                    ],
                    "correct_answer": 1
                },
                {
                    "id": 6,
                    "question": "What is a neural network?",
                    "options": [
                        "A computer network",
                        "A biological brain",
                        "A mathematical model inspired by biological neurons",
                        "A type of computer memory"
                    ],
                    "correct_answer": 2
                },
                {
                    "id": 7,
                    "question": "What is computer vision?",
                    "options": [
                        "Wearing computer glasses",
                        "The ability of computers to understand visual information",
                        "A type of display",
                        "A visualization tool"
                    ],
                    "correct_answer": 1
                },
                {
                    "id": 8,
                    "question": "What is clustering?",
                    "options": [
                        "Grouping similar data points",
                        "Creating backup copies",
                        "Connecting computers",
                        "Organizing files"
                    ],
                    "correct_answer": 0
                },
                {
                    "id": 9,
                    "question": "What is bias in machine learning?",
                    "options": [
                        "Personal preference",
                        "Systematic error in the model",
                        "Political opinion",
                        "User feedback"
                    ],
                    "correct_answer": 1
                },
                {
                    "id": 10,
                    "question": "What is overfitting?",
                    "options": [
                        "Wearing clothes too tight",
                        "Model performs well on training data but poorly on new data",
                        "Using too much data",
                        "Training for too long"
                    ],
                    "correct_answer": 1
                }
            ]
        }

        materials = {
            "doc_ids": ["ai_basics_001", "ml_intro_002", "neural_nets_003"],
            "doc_titles": [
                "Introduction to Artificial Intelligence",
                "Machine Learning Fundamentals",
                "Neural Networks Explained"
            ]
        }

        Quiz.objects.create(
            title="AI Fundamentals Quiz",
            materials_json=materials,
            questions_json=demo_quiz
        )

        self.stdout.write(self.style.SUCCESS('Successfully seeded demo data')) 