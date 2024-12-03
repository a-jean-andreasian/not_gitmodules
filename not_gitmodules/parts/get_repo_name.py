def extract_repo_name_from_url(repo_url: str):
    if repo_url.endswith('.git'):
        repo_url = repo_url.split('.git')[0]
    return repo_url.split('/')[-1]
