from agents import research_agent, writer_agent, reviewer_agent

topic = input("Enter topic: ")

print("\nResearching...\n")

research = research_agent(topic)

print("Research Result:\n")
print(research)

print("\nWriting article...\n")

article = writer_agent(topic, research)

print("Draft Article:\n")
print(article)

print("\nReviewing article...\n")

final_article = reviewer_agent(article)

print("Final Article:\n")
print(final_article)