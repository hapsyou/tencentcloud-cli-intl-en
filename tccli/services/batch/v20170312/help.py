# -*- coding: utf-8 -*-
DESC = "batch-2017-03-12"
INFO = {
  "DescribeCvmZoneInstanceConfigInfos": {
    "params": [
      {
        "name": "Filters",
        "desc": "Filter.\n<li> zone - String - Required: No - (Filter) Filter by availability zone.</li>\n<li> instance-family - String - Required: No - (Filter) Filter by model family such as S1, I1, and M1.</li>\n<li> instance-type - String - Required: No - (Filter) Filter by model.</li>\n<li> instance-charge-type - String - Required: No - (Filter) Filter by instance billing method. ( POSTPAID_BY_HOUR: pay-as-you-go | SPOTPAID: bidding.)  </li>"
      }
    ],
    "desc": "This API is used to get the model configuration information of the availability zone of BatchCompute."
  },
  "CreateTaskTemplate": {
    "params": [
      {
        "name": "TaskTemplateName",
        "desc": "Task template name"
      },
      {
        "name": "TaskTemplateInfo",
        "desc": "Task template content with the same parameter requirements as the task"
      },
      {
        "name": "TaskTemplateDescription",
        "desc": "Task template description"
      }
    ],
    "desc": "This API is used to create a task template."
  },
  "TerminateComputeNode": {
    "params": [
      {
        "name": "EnvId",
        "desc": "Compute environment ID"
      },
      {
        "name": "ComputeNodeId",
        "desc": "Compute node ID"
      }
    ],
    "desc": "This API is used to terminate a compute node.\nTermination is allowed for nodes in the CREATED, CREATION_FAILED, RUNNING or ABNORMAL state."
  },
  "DeleteJob": {
    "params": [
      {
        "name": "JobId",
        "desc": "Job ID"
      }
    ],
    "desc": "This API is used to delete a job.\nDeleting a job is equivalent to deleting all the information related to the job. After successful deletion, all information related to the job cannot be queried.\nThe job to be deleted must be in a completed state, and all task instances contained in it must also be in a completed state; otherwise, the operation will be prohibited. The completed state can be either SUCCEED or FAILED."
  },
  "DescribeAvailableCvmInstanceTypes": {
    "params": [
      {
        "name": "Filters",
        "desc": "Filter.\n<li> zone - String - Required: No - (Filter) Filter by availability zone.</li>\n<li> instance-family - String - Required: No - (Filter) Filter by model family such as S1, I1, and M1.</li>"
      }
    ],
    "desc": "This API is used to view the information of available CVM model configurations."
  },
  "AttachInstances": {
    "params": [
      {
        "name": "EnvId",
        "desc": "Compute environment ID"
      },
      {
        "name": "Instances",
        "desc": "List of instances that added to the compute environment"
      }
    ],
    "desc": "This API is used to add existing instances to the compute environment.\nConsiderations: <br/>\n1. The instance should not be in the batch compute system.<br/>\n2. The instance status should be 'running'.<br/>\n3. It supports dedicated CVMs and pay-as-you-go instances that billed on an hourly basis. Spot instances are not supported.<b/>\n\nFor instances added to the compute environment, their UserData will be reset and the operating systems will be reinstalled."
  },
  "CreateComputeEnv": {
    "params": [
      {
        "name": "ComputeEnv",
        "desc": "Compute environment information"
      },
      {
        "name": "Placement",
        "desc": "Location information"
      },
      {
        "name": "ClientToken",
        "desc": "The string used to guarantee the idempotency of the request, which is generated by the user and must be unique for different requests. The maximum length is 64 ASCII characters. If this parameter is not specified, the idempotency of the request cannot be guaranteed."
      }
    ],
    "desc": "This API is used to create a compute environment."
  },
  "DescribeComputeEnvs": {
    "params": [
      {
        "name": "EnvIds",
        "desc": "Compute environment ID"
      },
      {
        "name": "Filters",
        "desc": "Filter\n<li> zone - String - Required: No - (Filter) Filter by availability zone.</li>\n<li> env-id - String - Required: No - (Filter) Filter by compute environment ID.</li>\n<li> env-name - String - Required: No - (Filter) Filter by compute environment name.</li>"
      },
      {
        "name": "Offset",
        "desc": "Offset"
      },
      {
        "name": "Limit",
        "desc": "Number of returned results"
      }
    ],
    "desc": "This API is used to view the list of compute environments."
  },
  "DetachInstances": {
    "params": [
      {
        "name": "EnvId",
        "desc": "Compute environment ID"
      },
      {
        "name": "InstanceIds",
        "desc": "Instance ID list"
      }
    ],
    "desc": "This API is used to remove instances that from compute environment. "
  },
  "DescribeTaskLogs": {
    "params": [
      {
        "name": "JobId",
        "desc": "Instance ID"
      },
      {
        "name": "TaskName",
        "desc": "Job name"
      },
      {
        "name": "TaskInstanceIndexes",
        "desc": "Set of task instances"
      },
      {
        "name": "Offset",
        "desc": "Starting task instance"
      },
      {
        "name": "Limit",
        "desc": "Maximum number of task instances"
      }
    ],
    "desc": "This API is used to get the standard outputs and standard error logs of multiple task instances."
  },
  "TerminateJob": {
    "params": [
      {
        "name": "JobId",
        "desc": "Instance ID"
      }
    ],
    "desc": "This API is used to terminate an instance.\nTermination is prohibited if an instance is in the \"SUBMITTED\" state and does not take effect if it is in the \"SUCCEED\" state.\nInstance termination is an asynchronous process, and the time it takes to complete the entire process is directly proportional to the total number of tasks. The effect of terminating an instance is equivalent to performing the TerminateTaskInstance operation on all the task instances contained in the job. For more information on the specific effect and usage, see TerminateTaskInstance."
  },
  "DescribeTask": {
    "params": [
      {
        "name": "JobId",
        "desc": "Instance ID"
      },
      {
        "name": "TaskName",
        "desc": "Task name"
      },
      {
        "name": "Offset",
        "desc": "Offset"
      },
      {
        "name": "Limit",
        "desc": "Number of returned results. Default value: 100. Maximum value: 1,000."
      },
      {
        "name": "Filters",
        "desc": "Filter as detailed below:\n<li> task-instance-type - String - Required: No - (Filter) Filter by task instance state. (SUBMITTED: submitted; PENDING: pending; RUNNABLE: runnable; STARTING: starting; RUNNING: running; SUCCEED: succeeded; FAILED: failed; FAILED_INTERRUPTED: instance retained after failure).</li>"
      }
    ],
    "desc": "This API is used to query the details of a specified task, including information of the task instances inside the task."
  },
  "DescribeComputeEnv": {
    "params": [
      {
        "name": "EnvId",
        "desc": "Compute environment ID"
      }
    ],
    "desc": "This API is used to query compute environment details."
  },
  "DescribeJob": {
    "params": [
      {
        "name": "JobId",
        "desc": "Instance ID"
      }
    ],
    "desc": "This API is used to view the details of a job, including internal task (Task) and dependency (Dependence) information."
  },
  "DescribeComputeEnvActivities": {
    "params": [
      {
        "name": "EnvId",
        "desc": "Compute environment ID"
      },
      {
        "name": "Offset",
        "desc": "Offset"
      },
      {
        "name": "Limit",
        "desc": "Number of returned results"
      },
      {
        "name": "Filters",
        "desc": "Filter\n<li> compute-node-id - String - Required: No - (Filter) Filter by compute node ID.</li>"
      }
    ],
    "desc": "This API is used to query the information of activities in the compute environment."
  },
  "TerminateComputeNodes": {
    "params": [
      {
        "name": "EnvId",
        "desc": "Compute environment ID"
      },
      {
        "name": "ComputeNodeIds",
        "desc": "List of compute node IDs"
      }
    ],
    "desc": "This API is used to terminate compute nodes in batches. It is not allowed to repeatedly terminate the same node."
  },
  "DescribeTaskTemplates": {
    "params": [
      {
        "name": "TaskTemplateIds",
        "desc": "Job template ID"
      },
      {
        "name": "Filters",
        "desc": "Filter\n<li> task-template-name - String - Required: No - (Filter) Filter by task template name.</li>"
      },
      {
        "name": "Offset",
        "desc": "Offset"
      },
      {
        "name": "Limit",
        "desc": "Number of returned results"
      }
    ],
    "desc": "This API is used to query the information of task templates."
  },
  "DescribeInstanceCategories": {
    "params": [],
    "desc": "Currently, CVM instance families are classified into different category, and each category contains several instance families. This API is used to query the instance category information."
  },
  "DeleteTaskTemplates": {
    "params": [
      {
        "name": "TaskTemplateIds",
        "desc": "This API is used to delete task template information."
      }
    ],
    "desc": "This API is used to delete task template information."
  },
  "TerminateTaskInstance": {
    "params": [
      {
        "name": "JobId",
        "desc": "Instance ID"
      },
      {
        "name": "TaskName",
        "desc": "Task name"
      },
      {
        "name": "TaskInstanceIndex",
        "desc": "Task instance index"
      }
    ],
    "desc": "This API is used to terminate a task instance.\nTask instances in the \"SUCCEED\" or \"FAILED\" state will not be processed.\nTask instances in the \"SUBMITTED\", \"PENDING\", or \"RUNNABLE\" state will be set to the \"FAILED\" state.\nFor task instances in the \"STARTING\", \"RUNNING\", or \"FAILED_INTERRUPTED\" state, there will be two cases: if no compute environment is specified, the CVM instance will be terminated first, and then the state will be set to \"FAILED\"; if a compute environment's EnvId is specified, the state of the task instances will be set to \"FAILED\" first, and then the CVM instance that performs the task will be restarted. Both cases takes a certain amount of time to be completed.\nFor task instances in the \"FAILED_INTERRUPTED\" state, the related resources and quotas will be released only after the termination actually succeeds."
  },
  "ModifyComputeEnv": {
    "params": [
      {
        "name": "EnvId",
        "desc": "Compute environment ID"
      },
      {
        "name": "DesiredComputeNodeCount",
        "desc": "Number of desired compute nodes"
      },
      {
        "name": "EnvName",
        "desc": "Compute environment name"
      },
      {
        "name": "EnvDescription",
        "desc": "Compute environment description"
      },
      {
        "name": "EnvData",
        "desc": "Compute environment attributes"
      }
    ],
    "desc": "This API is used to modify the attributes of a compute environment."
  },
  "DescribeJobSubmitInfo": {
    "params": [
      {
        "name": "JobId",
        "desc": "Instance ID"
      }
    ],
    "desc": "This API is used to query the submission information of the specified job, with the return including the job submission information used as input parameters in the JobId and SubmitJob APIs."
  },
  "DescribeComputeEnvCreateInfo": {
    "params": [
      {
        "name": "EnvId",
        "desc": "Compute environment ID"
      }
    ],
    "desc": "Views compute environment creation information."
  },
  "SubmitJob": {
    "params": [
      {
        "name": "Placement",
        "desc": "Location information of the submitted job. This parameter allows you to specify information such as the availability zone of the CVM instance with which the job is associated."
      },
      {
        "name": "Job",
        "desc": "Job information"
      },
      {
        "name": "ClientToken",
        "desc": "The string used to guarantee the idempotency of the request, which is generated by the user and must be unique for different requests. The maximum length is 64 ASCII characters. If this parameter is not specified, the idempotency of the request cannot be guaranteed."
      }
    ],
    "desc": "This API is used to submit a instance."
  },
  "DescribeComputeEnvCreateInfos": {
    "params": [
      {
        "name": "EnvIds",
        "desc": "Compute environment ID"
      },
      {
        "name": "Filters",
        "desc": "Filter\n<li> zone - String - Required: No - (Filter) Filter by availability zone.</li>\n<li> env-id - String - Required: No - (Filter) Filter by compute environment ID.</li>\n<li> env-name - String - Required: No - (Filter) Filter by compute environment name.</li>"
      },
      {
        "name": "Offset",
        "desc": "Offset"
      },
      {
        "name": "Limit",
        "desc": "Number of returned results"
      }
    ],
    "desc": "This API is used to view the list of information of compute environment creation, including name, description, type, environment parameters, notifications, and number of desired nodes."
  },
  "DescribeJobs": {
    "params": [
      {
        "name": "JobIds",
        "desc": "Instance ID"
      },
      {
        "name": "Filters",
        "desc": "Filter\n<li> job-id - String - Required: No - (Filter) Filter by job ID.</li>\n<li> job-name - String - Required: No - (Filter) Filter by job name.</li>\n<li> job-state - String - Required: No - (Filter) Filter by job state.</li>\n<li> zone - String - Required: No - (Filter) Filter by availability zone.</li>"
      },
      {
        "name": "Offset",
        "desc": "Offset"
      },
      {
        "name": "Limit",
        "desc": "Number of returned results"
      }
    ],
    "desc": "This API is used to query the overview information of several instances."
  },
  "DeleteComputeEnv": {
    "params": [
      {
        "name": "EnvId",
        "desc": "Compute environment ID"
      }
    ],
    "desc": "This API is used to delete a compute environment."
  },
  "ModifyTaskTemplate": {
    "params": [
      {
        "name": "TaskTemplateId",
        "desc": "Job template ID"
      },
      {
        "name": "TaskTemplateName",
        "desc": "Job template name"
      },
      {
        "name": "TaskTemplateDescription",
        "desc": "Job template description"
      },
      {
        "name": "TaskTemplateInfo",
        "desc": "Job template information"
      }
    ],
    "desc": "This API is used to modify a task template."
  },
  "RetryJobs": {
    "params": [
      {
        "name": "JobIds",
        "desc": "List of instance IDs."
      }
    ],
    "desc": "This API is used to retry the failing task instance in instances.\nJob retry is supported only if a job is in the \"FAILED\" state. After the retry operation succeeds, the instance will retry the failing task instances in each task in turn according to the task dependencies specified in the \"DAG\". The history information of the task instances will be reset, the instances will participate in subsequent scheduling and execution as if they are run for the first time."
  }
}