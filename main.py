import subprocess

def run_ffuf(target_url, wordlist_path, output_dir, status_codes):
    try:
        # Define the ffuf command
        ffuf_command = [
            "ffuf",
            "-u", target_url,
            "-w", wordlist_path,
            "-o", output_dir,
            "-t", "1",  # Number of threads (adjust as needed)
            "-c",       # Colorize the output
        ]

        # Add filters for specific status codes
        for code in status_codes:
            ffuf_command.extend(["--fc",str(code)])

        # Execute the ffuf command
        subprocess.run(ffuf_command, check=True)

    except subprocess.CalledProcessError as e:
        print(f"Error running ffuf: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    target_url = "https://afit.edu.ng/FUZZ"  # Replace with your target URL
    wordlist_path = "directory-list-2.3-medium.txt"         # Replace with the path to your wordlist file
    output_dir = "output"             # Replace with the desired output directory
    status_codes = [403, 200, 405, 204]         # Specify the status codes you want to filter

    run_ffuf(target_url, wordlist_path, output_dir, status_codes)
