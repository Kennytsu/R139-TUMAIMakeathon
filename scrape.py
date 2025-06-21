import os
import subprocess

def download_website(url, output_dir):
    """
    Downloads a website using wget.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    command = [
        "wsl",
        "wget",
        "--recursive",
        "--page-requisites",
        "--convert-links",
        "--adjust-extension",
        "--no-parent",
        "--directory-prefix", output_dir,
        url
    ]
    
    try:
        subprocess.run(command, check=True)
        print(f"Successfully downloaded {url} to {output_dir}")
    except subprocess.CalledProcessError as e:
        print(f"Error downloading website: {e}")
    except FileNotFoundError:
        print("Error: wsl or wget is not installed or not in the system's PATH.")

if __name__ == "__main__":
    website_url = "https://tel-aviv.diplo.de/il-de"
    download_dir = "downloaded_site"
    download_website(website_url, download_dir) 