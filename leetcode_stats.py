import requests
import sys
from collections import Counter

LEETCODE_GRAPHQL_URL = "https://leetcode.com/graphql"


def fetch_user_profile(username: str):
    query = """
    query getUserProfile($username: String!) {
      matchedUser(username: $username) {
        username
        submitStats: submitStatsGlobal {
          acSubmissionNum {
            difficulty
            count
            submissions
          }
        }
        profile {
          ranking
          reputation
          realName
          countryName
          userAvatar
        }
      }
    }
    """
    variables = {"username": username}
    resp = requests.post(
        LEETCODE_GRAPHQL_URL, json={"query": query, "variables": variables}
    )
    resp.raise_for_status()
    data = resp.json()
    return data.get("data", {}).get("matchedUser", None)


def fetch_recent_submissions(username: str, limit: int = 1001):
    query = """
    query recentAcSubmissions($username: String!, $limit: Int!) {
      recentAcSubmissionList(username: $username, limit: $limit) {
        title
        titleSlug
        timestamp
      }
    }
    """
    variables = {"username": username, "limit": limit}
    resp = requests.post(
        LEETCODE_GRAPHQL_URL, json={"query": query, "variables": variables}
    )
    resp.raise_for_status()
    data = resp.json()
    return data.get("data", {}).get("recentAcSubmissionList", []) or []


def print_stats(username: str):
    user = fetch_user_profile(username)
    if not user:
        print(f"Could not find LeetCode user '{username}'.")
        return

    submit_stats = user.get("submitStats", {})
    ac_nums = submit_stats.get("acSubmissionNum", [])

    # Aggregate totals
    totals = {}
    total_solved = 0
    total_submissions = 0
    for entry in ac_nums:
        difficulty = entry.get("difficulty", "Unknown")
        count = entry.get("count", 0)
        subs = entry.get("submissions", 0)
        totals[difficulty] = {"count": count, "submissions": subs}
        if difficulty != "All":
            total_solved += count
            total_submissions += subs

    print("=" * 60)
    print(f"LeetCode Stats for: {username}")
    print("=" * 60)

    profile = user.get("profile", {}) or {}
    real_name = profile.get("realName") or ""
    country = profile.get("countryName") or ""
    ranking = profile.get("ranking", None)

    if real_name or country:
        line = "Profile:"
        if real_name:
            line += f" {real_name}"
        if country:
            line += f" ({country})"
        print(line)
    if ranking is not None:
        print(f"Global Ranking: {ranking:,}")
    print()

    print("Solved Problems by Difficulty:")
    for diff in ["Easy", "Medium", "Hard"]:
        info = totals.get(diff, {"count": 0, "submissions": 0})
        print(
            f"  {diff:6}: {info['count']:4d} solved, {info['submissions']:4d} submissions"
        )

    print()
    print(f"Total Solved: {total_solved}")
    if total_submissions > 0:
        acc_rate = 100.0 * total_solved / total_submissions
        print(f"Approx. Acceptance (AC count / total submissions): {acc_rate:.2f}%")
    print()

    # Recent AC submissions
    recent = fetch_recent_submissions(username, limit=1001)
    print(f"recent length {len(recent)}")
    print("Recent Accepted Submissions (up to last 1001):")
    if not recent:
        print("  No recent accepted submissions found.")
    else:
        # Count by title to show variety vs repeats
        title_counts = Counter(sub["title"] for sub in recent)
        for title, cnt in title_counts.most_common():
            print(f"  {title}  (AC x{cnt})")

    print("=" * 60)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python leetcode_stats.py <leetcode-username>")
        sys.exit(1)

    username = sys.argv[1].strip()
    print_stats(username)
