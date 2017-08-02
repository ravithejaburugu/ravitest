import java.net.URI;
import java.net.URISyntaxException;
import java.security.InvalidKeyException;
import java.util.Iterator;
import java.util.List;
import java.util.TreeSet;

import com.microsoft.azure.storage.CloudStorageAccount;
import com.microsoft.azure.storage.StorageException;
import com.microsoft.azure.storage.blob.CloudBlob;
import com.microsoft.azure.storage.blob.CloudBlobClient;
import com.microsoft.azure.storage.blob.CloudBlobContainer;
import com.microsoft.azure.storage.blob.CloudBlockBlob;


public class UploadingFilesToBlob extends ListOfDatasetURLS {
	
	private TreeSet set;
	
	public UploadingFilesToBlob() {
		this.set = listMethod();
	}
	/*
	 * For executing this code successfully a JAR is required named-"azure-storage-4.0.0"
	 * 
	 */
	
	public static final String storageConnectionString = "DefaultEndpointsProtocol=https;"
			+ "AccountName=randomtrees;"
			+ "AccountKey=wvNLlB2cSHhB0OFPRhIQDv+1QBJ1CnwFt+AGfQnL8rTyKTCG90t1Z+aCepe25aol6CKneJYgvHJl5gMtHON7TQ==;";
			//+ "EndpointSuffix=core.windows.net" ; 
	
   public  void method(String connectionStr, String ckankey , String datasourcety) throws InvalidKeyException, URISyntaxException, StorageException {
	   int counter = 0;
	   Iterator iter = set.iterator();
	   String urlname= iter.next().toString();
	   
	   String connectionString = String.format(storageConnectionString);
	  
		CloudStorageAccount account = CloudStorageAccount.parse(connectionString);
		CloudBlobClient client = account.createCloudBlobClient();
		CloudBlobContainer container = client.getContainerReference("dbpcontent");
	    CloudBlockBlob blob = container.getBlockBlobReference(urlname.substring(49));
	    
	    while (iter.hasNext()) {
			counter++;
			String url = urlname.toString();
			blob.startCopy(new URI(url));
			urlname = iter.next().toString();
			blob=container.getBlockBlobReference(urlname.substring(49));
	
			if(counter==5)
		{
			break;
		}
		
		}
	    account = null;
   }
	 

	
		
	

}






