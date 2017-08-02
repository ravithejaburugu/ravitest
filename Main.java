import java.net.URISyntaxException;
import java.security.InvalidKeyException;
import java.util.Scanner;

import com.microsoft.azure.storage.StorageException;

public class Main {

	
	public static void main(String[] args) throws InvalidKeyException {
		UploadingFilesToBlob uploadfilestoblob = new UploadingFilesToBlob();
		
		
		Scanner sc = new Scanner(System.in);
		System.out.print("Enter Azure Blob Storage connection string:- " );
		String azureConnection = sc.next();
		
		System.out.print("Enter CKAN key:- " );
		String CKAN = sc.next();
		
		System.out.print("Enter Data Source type(wikiInput/Ontology/Dataset/NLP dataset/DataIDs):- ");
		String dataSource = sc.next();
		
		if(dataSource.equalsIgnoreCase("dataset")) {
		try {
			uploadfilestoblob.method(azureConnection, CKAN, dataSource);
			System.out.println("Downloading file completed.");
		} catch (IllegalArgumentException | URISyntaxException | StorageException e) {
			// TODO Auto-generated catch block
			System.out.println();
			System.out.println("ERROR  - ..ISSUE WITH DOWNLOADING, MAY BE INVALID AZURE KEY OR CKAN KEY..");
			//e.printStackTrace();
		}
		}
		else {
			System.out.println("Invalid Datasource. Please try again..");
			
		}
	}
}
