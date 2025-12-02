from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
    aws_s3 as s3,   
)
from constructs import Construct

class MyCdkProjectStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "MyCdkProjectQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )

        MyL1Bucket = s3.CfnBucket(    #  創建一個L1的s3 Bucket construct實例
            self,
            "MyL1Bucket",       #  這是construct id，輸出yaml中的construct名字
            bucket_name="mmy-example-l1bucket",  # s3 bucket真正的名字(全球唯一)
            versioning_configuration={ #  物件被更新時不刪除而是分配新的版本ID
                "status": "Enabled"
            }
        )

        MyL2Bucket = s3.Bucket(
            self,
            "MyL2Bucket",
            bucket_name="mmy-example-l2bucket",
            versioned=True,
        )        