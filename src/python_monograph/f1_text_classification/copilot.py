import requests


def evaluate_and_star_repository(user_input):
    # Extract repository name and threshold from user input
    split_input = user_input.split("if the repository contains more than ")
    repository_name = split_input[0].split("about ")[-1].strip()
    threshold = int(split_input[1].split(" stars then")[0])

    # GitHub API URL
    url = f"https://api.github.com/repos/{repository_name}"

    # Fetch star count using requests
    response = requests.get(url)

    if response.status_code == 200:
        star_count = response.json()["stargazers_count"]
        star_decision = star_count > threshold
        print(f"Repository: {repository_name}, Stars: {star_count}")
        print(f"Star decision: {'Yes' if star_decision else 'No'} (starring not performed)")
        return repository_name, star_count, star_decision
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None, None, None


# Example usage
user_input = "I am hearing a lot about run-llama/llama_index nowadays, if the repository contains more than 10 stars then add a star from myself"
repository_name, star_count, star_decision = evaluate_and_star_repository(user_input)

if star_decision:
    print(f"The repository '{repository_name}' would have been starred if actual starring were implemented.")
