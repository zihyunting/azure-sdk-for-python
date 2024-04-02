---
page_type: sample
languages:
  - python
products:
  - azure-ai-vision-face
urlFragment: face-samples
---

# Azure Face client library for Python Samples

These are code samples that show common scenario operations with the Azure Face client library.
The async versions of the samples (the python sample files appended with `_async`) show asynchronous operations.

Several Azure Face Python SDK samples are available to you in the SDK's GitHub repository. These samples provide example code for additional scenarios commonly encountered while working with Face:

* [samples_authentication.py](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/face/azure-ai-vision-face/samples/samples_authentication.py) ([async version](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/face/azure-ai-vision-face/samples/samples_authentication_async.py)) - Examples for authenticating and creating the client:
    * From a key
    * From Microsoft Entra ID

* [samples_face_detection.py](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/face/azure-ai-vision-face/samples/samples_face_detection.py) ([async version](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/face/azure-ai-vision-face/samples/samples_face_detection_async.py)) - Examples for detecting human faces in an image:
    * From a binary data
    * From a URL

<!--
* [blob_samples_containers.py](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/storage/azure-storage-blob/samples/blob_samples_containers.py) ([async version](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/storage/azure-storage-blob/samples/blob_samples_containers_async.py)) - Examples for interacting with containers:
    * Create a container and delete containers
    * Set metadata on containers
    * Get container properties
    * Acquire a lease on container
    * Set an access policy on a container
    * Upload, list, delete blobs in container
    * Get the blob client to interact with a specific blob

* [blob_samples_common.py](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/storage/azure-storage-blob/samples/blob_samples_common.py) ([async version](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/storage/azure-storage-blob/samples/blob_samples_common_async.py)) - Examples common to all types of blobs:
    * Create a snapshot
    * Delete a blob snapshot
    * Soft delete a blob
    * Undelete a blob
    * Acquire a lease on a blob
    * Copy a blob from a URL

* [blob_samples_directory_interface.py](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/storage/azure-storage-blob/samples/blob_samples_directory_interface.py) - Examples for interfacing with Blob storage as if it were a directory on a filesystem:
    * Copy (upload or download) a single file or directory
    * List files or directories at a single level or recursively
    * Delete a single file or recursively delete a directory

* [blob_samples_batch_delete_blobs.py](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/storage/azure-storage-blob/samples/blob_samples_batch_delete_blobs.py) - Examples for batch
deleting blobs
    * Delete multiple blobs at the same time.

* [blob_samples_container_access_policy.py](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/storage/azure-storage-blob/samples/blob_samples_container_access_policy.py) ([async version](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/storage/azure-storage-blob/samples/blob_samples_container_access_policy_async.py)) - Examples to
get and set access policies:
    * Get and Set container Access Policy

* [blob_samples_copy_blob.py](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/storage/azure-storage-blob/samples/blob_samples_copy_blob.py) ([async version](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/storage/azure-storage-blob/samples/blob_samples_copy_blob_async.py)) - Examples to start and abort copy:
    * Start a copy from url and abort it.

* [blob_samples_enumerate_blobs.py](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/storage/azure-storage-blob/samples/blob_samples_enumerate_blobs.py) ([async version](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/storage/azure-storage-blob/samples/blob_samples_enumerate_blobs_async.py)) - Example to enumerate blobs
    * List all the blobs in a container.

* [blob_samples_walk_blob_hierarchy.py](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/storage/azure-storage-blob/samples/blob_samples_walk_blob_hierarchy.py) ([async version](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/storage/azure-storage-blob/samples/blob_samples_walk_blob_hierarchy_async.py)) - Example to walk through containers and blobs in a hierarchical structure.
    * Walk through the container.

* [blob_samples_network_activity_logging.py](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/storage/azure-storage-blob/samples/blob_samples_network_activity_logging.py) - Examples to enable logging to the console.
    * Log the network activity at different levels.

* [blob_samples_proxy_configuration.py](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/storage/azure-storage-blob/samples/blob_samples_proxy_configuration.py) - Examples to work with a proxy.
    * Work with a proxy using the storage account.

* [forecasting_in_vs_code_with_blob.ipynb](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/storage/azure-storage-blob/samples/forecasting_in_vs_code_with_blob.ipynb) - An end-to-end sample and writeup on leveraging blobs as part of an Azure data infrastructure.
    * Integrate blob with other Azure Services such as App Insights, and utilize it as a tool for data experimentation.
-->

## Prerequisites
* Python 3.8 or later is required to use this package
* You must have an [Azure subscription](https://azure.microsoft.com/free/) and an [Face APIs account](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/overview-identity)
to run these samples.

## Setup

1. Install the Face client library for Python with [pip](https://pypi.org/project/pip/):

```bash
pip install azure-ai-vision-face
```

2. Clone or download this sample repository
3. Open the sample folder in Visual Studio Code or your IDE of choice.

## Running the samples

1. Open a terminal window and `cd` to the directory that the samples are saved in.
2. Set the environment variables specified in the sample file you wish to run.
3. Follow the usage described in the file, e.g. `python samples_face_detection.py`

## Next steps

Check out the [API reference documentation](https://aka.ms/azsdk-python-face-ref) to learn more about what you can do
with the Azure Face client library.
