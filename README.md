**Enron Email Analysis - Big Data Cloud Project**

**Abstract**

The objective of this project is to solve a Big Data problem on the Cloud. This includes data collection, implementation, and performance analysis of an end-to-end application to analyze the Enron Email Dataset. The analysis identifies key email senders, communication patterns, and provides insight into possible fraudulent activities.

**1\. Problem Description**

The Enron Email Dataset contains emails from over 158 employees, which were made public during the investigation into the Enron scandal. The dataset is large, unstructured, and difficult to process with conventional tools. The problem is to extract valuable insights, such as top senders, recipients, and potential indicators of fraudulent activity.

**2\. Need for Big Data and Cloud**

The dataset size is around 1.7 GB and consists of over 600,000 emails. Handling and processing such large datasets require Big Data tools and Cloud infrastructure. Google Cloud Dataproc and Hadoop were chosen to manage the distributed storage and parallel processing. Without such infrastructure, it would be infeasible to process this dataset on a single machine.

**3\. Data Description**

- **Source:** The Enron Email Dataset is available on Kaggle.
- **Size:** Approximately 1.7 GB with over 600,000 emails.
- **Structure:** Each email contains metadata like 'From', 'To', 'Date', and 'Message'.
- **Storage:** The dataset is stored in Google Cloud Storage for distributed access.

**4\. Description of the Application**

- **Programming Models:** Spark and Hadoop MapReduce.
- **Platform:** Google Cloud Dataproc.
- **Infrastructure:** The cluster is set up with 1 master node and 2 or 4 worker nodes for performance analysis.

**5\. Software Design**

- **Architectural Design:** Data is stored on Google Cloud Storage and processed on Google Cloud Dataproc using PySpark.
- **Code Baseline:** PySpark script email_analysis.py was written to extract relevant information from the emails, such as the top senders, top recipients, and email frequencies.
- **Dependencies:** PySpark, Google Cloud SDK, Hadoop, and necessary Google Cloud
- libraries.

**6\. Usage**

**1\. Data Upload:** Upload the Enron Email Dataset to the Google Cloud Storage bucket.

**2.Enable Services:**

gcloud services enable compute.googleapis.com dataproc.googleapis.com storage.googleapis.com

**  
3 Upload your Enron email file:** (assume it’s named "emails.csv")

gsutil cp /path/to/your/emails.csv gs://river-inquiry-440619-n8/input/emails.csv

Note: If you don't have the "emails.csv" file, download it from Kaggle and place it on your local machine.

**3.Setup:** Create a Dataproc cluster with the 2 nodes using the following command:

gcloud dataproc clusters create enron-cluster \\--region=europe-southwest1 \\--num-workers=2

**4.Script Upload:** Upload the email_analysis.py script to the Cloud Storage bucket using the command:

gsutil cp email_analysis.py gs://river-inquiry-440619-n8/scripts/

**5.Run the Job:** Run the email analysis on the Dataproc cluster:

gcloud dataproc jobs submit pyspark gs://river-inquiry-440619n8/scripts/email_analysis.py\\--cluster=enron-cluster \\--region=europe-southwest1

**6.Setup:** Create a Dataproc cluster with the 4 nodes using the following command:
gcloud dataproc clusters create enron-cluster \\--region=europe-southwest1 \\--num-workers=4


**7.View Results:** The output files can be found in the following Google Cloud Storage path:

gsutil ls gs://river-inquiry-440619-n8/output/email_analysis_results/  
<br/>gsutil cat gs://river-inquiry-440619-n8/output/email_analysis_results/part-00000-a71a002e-9821-4896-a6d3-8175a7259bf5-c000.csv | head -n 10  
<br/>0.csv | head -n 10

<Kay.Mann@enron.com>,<Kay.Mann@enron.com>,1482

<Matthew.Lenhart@enron.com>,<Matthew.Lenhart@enron.com>,870

<Jeff.Dasovich@enron.com>,<Jeff.Dasovich@enron.com>,637

<Vince.J.Kaminski@enron.com>,<Vince.J.Kaminski@enron.com>,566

<Eric.Bass@enron.com>,<Eric.Bass@enron.com>,436

<Sara.Shackleton@enron.com>,<Sara.Shackleton@enron.com>,348

<Tana.Jones@enron.com>,<Tana.Jones@enron.com>,345

<Chris.Germany@enron.com>,<Chris.Germany@enron.com>,304

<erwollam@hotmail.com>,<erwollam@hotmail.com>,290

<Kim.Ward@enron.com>,<Kim.Ward@enron.com>,286

**7\. Performance Evaluation**

The performance of the analysis was evaluated using 2 and 4 worker nodes to measure the impact on execution time.

- **2 Nodes:**
  - Total Processing Time: **3 minutes 11 seconds**
  - Total Valid Emails Processed: **32,303**
- **4 Nodes:**
  - Total Processing Time: **2 minutes 19 seconds**
  - Total Valid Emails Processed: **32,303**

**Observation:** The analysis shows a significant reduction in processing time when moving from 2 nodes to 4 nodes, demonstrating the scalability of the cloud-based distributed processing system.

1. **Advanced Features**

- **Data Parallelism:** Distributed processing using Spark and Hadoop.
- **Cluster Scalability:** Cluster size is increased from 2 to 4 worker nodes to demonstrate scalability.
- **Optimization:** Use of Dataproc properties and resource management to optimize performance.
- **Fault Tolerance:** Dataproc provides fault tolerance with auto-retries for failed jobs.

**9\. Conclusions**

- The project successfully demonstrates the use of Big Data and Cloud to analyze large datasets.
- Key insights were extracted, such as identifying top senders and recipients from the Enron Email Dataset.
- Performance improved as the cluster size increased from 2 to 4 worker nodes.
- Lessons learned include the importance of cloud resources, distributed processing, and resource optimization.

**10\. References**

- Enron Email Dataset from Kaggle  
    <https://www.kaggle.com/datasets/wcukierski/enron-email-dataset>