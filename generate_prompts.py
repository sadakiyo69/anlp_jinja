import os
from jinja2 import Environment, FileSystemLoader

def main():
    env = Environment(loader=FileSystemLoader("."))

    template = env.get_template("movie_review_prompt.j2")

    examples = [
        {
            "review": "Altohugh the move was visually stunning, the storyline was weak.",
            "format": "bullet",
            "output": """{
      "sentiment": "neutral",
      "aspects": ["visuals", "plot"],
      "reasoning": "Positive visuals but weak story balances sentiment."
    }"""
        },
        {
            "review": "Utterly terrible acting performances and boring plot.",
            "format": "bullet",
            "output": """{
      "sentiment": "negative",
      "aspects": ["acting", "plot"],
      "reasoning": "Both, acting and plotting, are heavily criticized"
    }"""
        },
        {
            "review": "An absolute masterpiece of a film, with emotional depth and outstanding performances.",
            "format": "json",
            "output": """{
      "sentiment": "positive",
      "aspects": ["acting", "emotional depth"],
      "reasoning": "Stronlgy praised acting and emotional depth."
    }"""
        },
        {
            "review": "Best acting, ive ever seen",
            "format": "json",
            "output": """{
          "sentiment": "",
          "aspects": [""],
          "reasoning": "Praised acting."
        }"""
        }
    ]

    test_reviews = [
        {
            "review": "The cinematography was beautiful, yet the pacing was slow.",
            "format": "json"
        },
        {
            "review": "Sadly, the ending was a disappointment, because I really loved the characters.",
            "format": "bullet"
        },
        {
            "review": "Completely boring, one of the worst films I have ever seen.",
            "format": "json"
        }
    ]


    print("HERE BEGINS THE GENERATION OF PROPMTS---------\n")
    for i, item in enumerate(test_reviews, 1):
        prompt = template.render(
            include_reasoning=True,
            examples=examples,
            target_review=item["review"],
            output_format=item["format"]
        )

        print("\n" + "=" * 80)
        print(f'PROMPT {i} ({item["format"].upper()})')
        print("=" * 80)
        print(prompt)


if __name__ == "__main__":
    main()