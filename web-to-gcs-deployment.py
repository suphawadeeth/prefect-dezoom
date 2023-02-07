from prefect.deployments import Deployment
from etl_web_to_gcs_q4 import etl_web_to_gcs
from prefect.filesystems import GitHub 

github_block = GitHub.load("dezoom-prefect")

deployment = Deployment.build_from_flow(
     flow=etl_web_to_gcs,
     name="github-example",
     storage=github_block,
     entrypoint="/Users/kt/Desktop/DEzoom/homework/prefect-dezoom/etl_web_to_gcs_q4.py:etl_web_to_gcs")

if __name__ == "__main__":
    deployment.apply()