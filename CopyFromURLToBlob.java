
import java.net.URI;
import java.net.URISyntaxException;
import java.security.InvalidKeyException;
//import java.util.Scanner;
import java.util.Scanner;

import com.microsoft.azure.storage.CloudStorageAccount;
import com.microsoft.azure.storage.StorageException;
//import com.microsoft.azure.storage.blob.CloudBlob;
import com.microsoft.azure.storage.blob.CloudBlobClient;
import com.microsoft.azure.storage.blob.CloudBlobContainer;
import com.microsoft.azure.storage.blob.CloudBlockBlob;


public class CopyFromURLToBlob {
	/*
	 * For executing this code successfully a JAR is required named-"azure-storage-4.0.0"
	 * 
	 */

	/*public static final String storageConnectionString =  "DefaultEndpointsProtocol=https;"
			+ "AccountName=randomtrees;"
			+ "AccountKey=wvNLlB2cSHhB0OFPRhIQDv+1QBJ1CnwFt+AGfQnL8rTyKTCG90t1Z+aCepe25aol6CKneJYgvHJl5gMtHON7TQ==;";
			//+ "EndpointSuffix=core.windows.net" ; 
	*/
	public void method(String connectionStr, String ckankey , String datasourcety) throws  IllegalArgumentException, URISyntaxException, StorageException {
	  // Scanner scanner = new Scanner(System.in);
	  
	   String connectionString =  connectionStr;
	   String CKANKey =  ckankey;
	   String dataSourceType =  datasourcety; 
	   
	   
		CloudStorageAccount account;
		try {
			account = CloudStorageAccount.parse(connectionString);CloudBlobClient client = account.createCloudBlobClient();
			CloudBlobContainer container = client.getContainerReference("dbpcontent/Ontology");
			CloudBlockBlob blob = container.getBlockBlobReference("latest.txt");
		
			String url = "https://dumps.wikimedia.org/enwiki/20170620/enwiki-20170620-pages-articles-multistream-index.txt.bz2";
			blob.startCopy(new URI(url));
			
		} catch (InvalidKeyException e) {
			// TODO Auto-generated catch block
			System.out.println("Invalid key.");
			e.printStackTrace();
		}
		

	   
	  
   }
	
	

}



