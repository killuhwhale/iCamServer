'''
Install docker and run the two images...

docker images list
docker tag espcam_esp32server:latest killuhwhale/camserver_api:latest
docker tag espcam_frontend:latest killuhwhale/camserver:latest
docker push killuhwhale/camserver:latest
docker push killuhwhale/camserver_api:latest


docker tag local-image:tagname new-repo:tagname
docker push new-repo:tagname
'''
import argparse
import subprocess


def start():
    print("Starting")
    # Install docker on CPU
    # Pip install docker
    # Once docker is installed
    # Run script with docker to run image

    # print("Pulling")

    # dpull_front = subprocess.run(["docker", "compose", "pull", "esp32server"],
    #                              capture_output=True, universal_newlines=True)
    # print(dpull_front.stdout)
    # print(dpull_front.stderr)
    # dpull_api = subprocess.run(["docker", "compose", "pull", "frontend"],
    #                            capture_output=True, universal_newlines=True)

    # print(dpull_api.stdout)
    # print(dpull_api.stderr)

    dc = subprocess.run(["docker", "compose", "up", "-d", "--no-build"],
                        capture_output=True, universal_newlines=True)

    print(dc.stdout)
    print(dc.stderr)


def stop():
    print("Stopping")
    dc = subprocess.run(["docker", "compose", "down"],
                        capture_output=True, universal_newlines=True)

    print(dc.stdout)
    print(dc.stderr)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="iCamServer Docker/ compose required.")
    parser.add_argument("-s", "--start", action="store_true",
                        help="Start iCamServer.")
    parser.add_argument("-q", "--quit", action="store_true",
                        help="Quit iCamServer.")
    args = parser.parse_args()
    if args.start:
        start()

    if args.quit:
        stop()
