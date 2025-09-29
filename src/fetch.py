from dataclasses import dataclass

import requests


@dataclass
class ContributionData:
    total_contributions: int
    total_weeks: int
    count_matrix: list[list[int]]
    level_matrix: list[list[str]]


def fetch_github_contributions(token: str) -> ContributionData:
    response = requests.post(
        "https://api.github.com/graphql",
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        },
        json={
            "query": """
                query {
                    viewer {
                        contributionsCollection {
                            contributionCalendar {
                                totalContributions
                                weeks {
                                    contributionDays {
                                        contributionCount
                                        contributionLevel
                                        date
                                    }
                                }
                            }
                        }
                    }
                }
            """
        },
    )

    if response.status_code != 200:
        raise Exception(f"Failed to fetch data from GitHub: {response.text}")

    calendar = (
        response.json()
        .get("data")
        .get("viewer")
        .get("contributionsCollection")
        .get("contributionCalendar")
    )
    total_contributions = calendar.get("totalContributions")
    total_weeks = len(calendar.get("weeks"))
    count_matrix = [
        [day.get("contributionCount") for day in week.get("contributionDays")]
        for week in calendar.get("weeks")
    ]
    level_matrix = [
        [day.get("contributionLevel") for day in week.get("contributionDays")]
        for week in calendar.get("weeks")
    ]

    return ContributionData(
        total_contributions, total_weeks, count_matrix, level_matrix
    )


if __name__ == "__main__":
    import os

    token = os.getenv("GITHUB_TOKEN")

    data = fetch_github_contributions(token)

    print(data.total_contributions)
    print(data.total_weeks)
    print(data.count_matrix)
    print(data.level_matrix)
