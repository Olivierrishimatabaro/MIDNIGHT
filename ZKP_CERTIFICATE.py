# Définition de la certification
class Certification:
    def __init__(self, title, issuer, topics, description):
        self.title = title
        self.issuer = issuer
        self.topics = topics
        self.description = description

    def display(self):
        print("="*40)
        print(f"🎓 Certification: {self.title}")
        print(f"🏫 Issuer: {self.issuer}")
        print("📚 Topics Covered:")
        for topic in self.topics:
            print(f" - {topic}")
        print(f"📝 Description: {self.description}")
        print("="*40)

# Ma certification ZKP / Privacy
zkpCertification = Certification(
    title="Privacy & Zero-Knowledge Development",
    issuer="Midnight Academy",
    topics=[
        "Privacy-first blockchain design",
        "Zero-Knowledge Proofs (ZKP)",
        "Selective disclosure",
        "Smart contracts with both public and private state",
        "Building privacy-preserving Web3 applications"
    ],
    description="Completed a specialized program focused on privacy-preserving technologies, " 
                "understanding cryptography in decentralized systems, and developing skills to create compliant, scalable, and secure blockchain solutions."
)

# Affichage
zkpCertification.display()
