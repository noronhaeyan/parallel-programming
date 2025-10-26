import asyncio
import random
import string
import aiofiles

async def generate_random_text(length=1000):
    """Generate random text of specified length with multiple lines"""
    words = ['lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur', 'adipiscing', 'elit',
             'sed', 'do', 'eiusmod', 'tempor', 'incididunt', 'ut', 'labore', 'et', 'dolore',
             'magna', 'aliqua', 'enim', 'ad', 'minim', 'veniam', 'quis', 'nostrud',
             'exercitation', 'ullamco', 'laboris', 'nisi', 'aliquip', 'ex', 'ea', 'commodo',
             'consequat', 'duis', 'aute', 'irure', 'in', 'reprehenderit', 'voluptate',
             'velit', 'esse', 'cillum', 'fugiat', 'nulla', 'pariatur', 'excepteur', 'sint',
             'occaecat', 'cupidatat', 'non', 'proident', 'sunt', 'culpa', 'qui', 'officia',
             'deserunt', 'mollit', 'anim', 'id', 'est', 'laborum']
    
    lines = []
    current_length = 0
    
    while current_length < length:
        # Generate a line with 10-20 words
        line_words = []
        words_in_line = random.randint(10, 20)
        
        for _ in range(words_in_line):
            word = random.choice(words)
            line_words.append(word)
        
        line = ' '.join(line_words)
        lines.append(line)
        current_length += len(line) + 1  # +1 for newline
    
    return '\n'.join(lines)

async def create_file(file_number):
    """Create a single file with random text"""
    filename = f"file{file_number}.txt"
    content = await generate_random_text(100000000)  # 2000 characters of text
    
    async with aiofiles.open(filename, 'w') as f:
        await f.write(content)
    
    print(f"Created {filename}")

async def main():
    """Create 10 files concurrently"""
    tasks = [create_file(i) for i in range(10,20)]
    await asyncio.gather(*tasks)
    print("All files created successfully!")

if __name__ == "__main__":
    asyncio.run(main())