import datetime


LIST_USERS = {
    "Users": [
        {
            "UserName": "example-user-0",
            "PasswordLastUsed": datetime.datetime(2019, 1, 1, 0, 0, 1),
            "CreateDate": datetime.datetime(2019, 1, 1, 0, 0, 1),
            "UserId": "AIDA00000000000000000",
            "Path": "/",
            "Arn": "arn:aws:iam::000000000000:user/example-user-0",
        },
        {
            "UserName": "example-user-1",
            "PasswordLastUsed": datetime.datetime(2019, 1, 1, 0, 0, 1),
            "CreateDate": datetime.datetime(2019, 1, 1, 0, 0, 1),
            "UserId": "AIDA00000000000000001",
            "Path": "/",
            "Arn": "arn:aws:iam::000000000000:user/example-user-1",
        },
    ],
}


LIST_GROUPS = {
    "Groups": [
        {
            "Path": "/",
            "CreateDate": datetime.datetime(2019, 1, 1, 0, 0, 1),
            "GroupId": "AGPA000000000000000000",
            "Arn": "arn:aws:iam::000000000000:group/example-group-0",
            "GroupName": "example-group-0",
        },
        {
            "Path": "/",
            "CreateDate": datetime.datetime(2019, 1, 1, 0, 0, 1),
            "GroupId": "AGPA000000000000000001",
            "Arn": "arn:aws:iam::000000000000:group/example-group-1",
            "GroupName": "example-group-1",
        },
    ],
}


LIST_POLICIES = {
    "Policies": [
        {
            "PolicyName": "example-policy-0",
            "PermissionsBoundaryUsageCount": 0,
            "CreateDate": datetime.datetime(2019, 1, 1, 0, 0, 1),
            "AttachmentCount": 0,
            "IsAttachable": True,
            "PolicyId": "ANPA00000000000000000",
            "DefaultVersionId": "v1",
            "Path": "/",
            "Arn": "arn:aws:iam::173840052742:policy/example-policy-0",
            "UpdateDate": datetime.datetime(2019, 1, 1, 0, 0, 1),
        },
        {
            "PolicyName": "example-policy-1",
            "PermissionsBoundaryUsageCount": 0,
            "CreateDate": datetime.datetime(2019, 1, 1, 0, 0, 1),
            "AttachmentCount": 0,
            "IsAttachable": True,
            "PolicyId": "ANPA00000000000000001",
            "DefaultVersionId": "v1",
            "Path": "/",
            "Arn": "arn:aws:iam::173840052742:policy/example-policy-1",
            "UpdateDate": datetime.datetime(2019, 1, 1, 0, 0, 1),
        },
    ],
}


LIST_ROLES = {
    "Roles": [
        {
            "AssumeRolePolicyDocument": {
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Action": "sts:AssumeRole",
                        "Effect": "Allow",
                        "Principal": {
                            "AWS": "arn:aws:iam::000000000000:root",
                        },
                    },
                ],
            },
            "MaxSessionDuration": 3600,
            "RoleId": "AROA00000000000000000",
            "CreateDate": datetime.datetime(2019, 1, 1, 0, 0, 1),
            "RoleName": "example-role-0",
            "Path": "/",
            "Arn": "arn:aws:iam::000000000000:role/example-role-0",
        },
        {
            "AssumeRolePolicyDocument": {
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Action": "sts:AssumeRole",
                        "Effect": "Allow",
                        "Principal": {
                            "AWS": "arn:aws:iam::000000000000:role/example-role-0",
                        },
                    },
                ],
            },
            "MaxSessionDuration": 3600,
            "RoleId": "AROA00000000000000001",
            "CreateDate": datetime.datetime(2019, 1, 1, 0, 0, 1),
            "RoleName": "example-role-1",
            "Path": "/",
            "Arn": "arn:aws:iam::000000000000:role/example-role-1",
        },
        {
            "AssumeRolePolicyDocument": {
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Action": "sts:AssumeRole",
                        "Effect": "Allow",
                        "Principal": {
                            "Service": "ec2.amazonaws.com",
                        },
                    },
                ],
            },
            "MaxSessionDuration": 3600,
            "RoleId": "AROA00000000000000002",
            "CreateDate": datetime.datetime(2019, 1, 1, 0, 0, 1),
            "RoleName": "example-role-2",
            "Path": "/",
            "Arn": "arn:aws:iam::000000000000:role/example-role-2",
        },
        {
            "AssumeRolePolicyDocument": {
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Action": "sts:AssumeRoleWithSAML",
                        "Effect": "Allow",
                        "Principal": {
                            "Federated": "arn:aws:iam::000000000000:saml-provider/ADFS",
                        },
                        "Condition": {
                            "StringEquals": {
                                "SAML:aud": "https://signin.aws.amazon.com/saml",
                            },
                        },
                    },
                ],
            },
            "MaxSessionDuration": 3600,
            "RoleId": "AROA00000000000000003",
            "CreateDate": datetime.datetime(2019, 1, 1, 0, 0, 1),
            "RoleName": "example-role-3",
            "Path": "/",
            "Arn": "arn:aws:iam::000000000000:role/example-role-3",
        },
    ],
}
