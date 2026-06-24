# NTRCA Math Quiz Engine
questions = [
    {
        "q": "f(t) = e^2t এর ল্যাপ্লাস ট্রান্সফর্ম কোনটি?",
        "options": "ক) 1/(s+2)  খ) 1/(s-2)  গ) 2/(s+2)",
        "answer": "খ",
        "explanation": "সূত্র: L{e^at} = 1/(s-a)। এখানে a=2।"
    },
    {
        "q": "ল্যাপ্লাস ট্রান্সফর্ম কোন ডোমেইনে কাজ করে?",
        "options": "ক) টাইম  খ) ফ্রিকোয়েন্সি  গ) ডিসট্যান্স",
        "answer": "খ",
        "explanation": "ল্যাপ্লাস ট্রান্সফর্ম টাইম ডোমেইন থেকে ফ্রিকোয়েন্সি ডোমেইনে রূপান্তর করে।"
    }
]

score = 0
for item in questions:
    print(f"\n{item['q']}")
    print(item['options'])
    ans = input("আপনার উত্তর (ক/খ/গ): ")
    if ans == item['answer']:
        print("সঠিক!")
        score += 1
    else:
        print(f"ভুল। সঠিক উত্তর: {item['answer']}. ব্যাখ্যা: {item['explanation']}")

print(f"\nকুইজ শেষ! আপনার মোট স্কোর: {score}/{len(questions)}")
