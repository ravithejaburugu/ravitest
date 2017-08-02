import java.nio.charset.MalformedInputException;
import java.util.ArrayList;
import java.util.List;
import java.util.TreeSet;

public class ListOfDatasetURLS {
	
	protected static String datasetURLS1 		="http://downloads.dbpedia.org/2016-10/core-i18n/en/2016-10_dataid_en.json";
	protected static String datasetURLS2		="http://downloads.dbpedia.org/2016-10/core-i18n/en/2016-10_dataid_en.ttl";
	protected static String datasetURLS3		="http://downloads.dbpedia.org/2016-10/core-i18n/en/_checksums.md5";
	protected static String datasetURLS4		="http://downloads.dbpedia.org/2016-10/core-i18n/en/anchor_text_en.tql.bz2";
	protected static String datasetURLS5		="http://downloads.dbpedia.org/2016-10/core-i18n/en/anchor_text_en.ttl.bz2";
	protected static String datasetURLS6		="http://downloads.dbpedia.org/2016-10/core-i18n/en/article_categories_en.tql.bz2";
	protected static String datasetURLS7		="http://downloads.dbpedia.org/2016-10/core-i18n/en/article_categories_en.ttl.bz2";
	protected static String datasetURLS8		="http://downloads.dbpedia.org/2016-10/core-i18n/en/article_categories_wkd_uris_en.tql.bz2";
	protected static String datasetURLS9		="http://downloads.dbpedia.org/2016-10/core-i18n/en/article_categories_wkd_uris_en.ttl.bz2";
	protected static String datasetURLS10		="http://downloads.dbpedia.org/2016-10/core-i18n/en/article_categories_sorted_en.ttl.bz2";
	protected static String datasetURLS11		="http://downloads.dbpedia.org/2016-10/core-i18n/en/article_templates_en.tql.bz2";
	protected static String datasetURLS12		="http://downloads.dbpedia.org/2016-10/core-i18n/en/article_templates_en.ttl.bz2";
	protected static String datasetURLS13		="http://downloads.dbpedia.org/2016-10/core-i18n/en/article_templates_nested_en.tql.bz2";
	protected static String datasetURLS14		="http://downloads.dbpedia.org/2016-10/core-i18n/en/article_templates_nested_en.ttl.bz2";
	protected static String datasetURLS15		="http://downloads.dbpedia.org/2016-10/core-i18n/en/category_labels_en.tql.bz2";
	protected static String datasetURLS16		="http://downloads.dbpedia.org/2016-10/core-i18n/en/category_labels_en.ttl.bz2";
	protected static String datasetURLS17		="http://downloads.dbpedia.org/2016-10/core-i18n/en/category_labels_sorted_en.ttl.bz2";
	protected static String datasetURLS18		="http://downloads.dbpedia.org/2016-10/core-i18n/en/category_labels_wkd_uris_en.tql.bz2";
	protected static String datasetURLS19		="http://downloads.dbpedia.org/2016-10/core-i18n/en/category_labels_wkd_uris_en.ttl.bz2";
	protected static String datasetURLS20		="http://downloads.dbpedia.org/2016-10/core-i18n/en/citation_data_en.tql.bz2";
	protected static String datasetURLS21		="http://downloads.dbpedia.org/2016-10/core-i18n/en/citation_data_en.ttl.bz2";
	protected static String datasetURLS22		="http://downloads.dbpedia.org/2016-10/core-i18n/en/citation_links_en.tql.bz2";
	protected static String datasetURLS23		="http://downloads.dbpedia.org/2016-10/core-i18n/en/citation_links_en.ttl.bz2";
	protected static String datasetURLS24		="http://downloads.dbpedia.org/2016-10/core-i18n/en/commons_page_links_en.tql.bz2";
	protected static String datasetURLS25		="http://downloads.dbpedia.org/2016-10/core-i18n/en/commons_page_links_en.ttl.bz2";
	protected static String datasetURLS26		="http://downloads.dbpedia.org/2016-10/core-i18n/en/disambiguations_en.tql.bz2";
	protected static String datasetURLS27		="http://downloads.dbpedia.org/2016-10/core-i18n/en/disambiguations_en.ttl.bz2";
	protected static String datasetURLS28		="http://downloads.dbpedia.org/2016-10/core-i18n/en/disambiguations_wkd_uris_en.tql.bz2";
	protected static String datasetURLS29		="http://downloads.dbpedia.org/2016-10/core-i18n/en/disambiguations_wkd_uris_en.ttl.bz2";
	protected static String datasetURLS30		="http://downloads.dbpedia.org/2016-10/core-i18n/en/download_complete_en.download-complete";
	protected static String datasetURLS31		="http://downloads.dbpedia.org/2016-10/core-i18n/en/equations_en.tql.bz2";
	protected static String datasetURLS32		="http://downloads.dbpedia.org/2016-10/core-i18n/en/equations_en.ttl.bz2";
	protected static String datasetURLS33		="http://downloads.dbpedia.org/2016-10/core-i18n/en/external_links_en.tql.bz2";
	protected static String datasetURLS34		="http://downloads.dbpedia.org/2016-10/core-i18n/en/external_links_en.ttl.bz2";
	protected static String datasetURLS35		="http://downloads.dbpedia.org/2016-10/core-i18n/en/external_links_wkd_uris_en.tql.bz2";
	protected static String datasetURLS36		="http://downloads.dbpedia.org/2016-10/core-i18n/en/external_links_wkd_uris_en.ttl.bz2";
	protected static String datasetURLS37		="http://downloads.dbpedia.org/2016-10/core-i18n/en/freebase_links_en.ttl.bz2";
	protected static String datasetURLS38		="http://downloads.dbpedia.org/2016-10/core-i18n/en/genders_en.tql.bz2";
	protected static String datasetURLS39		="http://downloads.dbpedia.org/2016-10/core-i18n/en/genders_en.ttl.bz2";
	protected static String datasetURLS40		="http://downloads.dbpedia.org/2016-10/core-i18n/en/genders_wkd_uris_en.tql.bz2";
	protected static String datasetURLS41		="http://downloads.dbpedia.org/2016-10/core-i18n/en/genders_wkd_uris_en.ttl.bz2";
	protected static String datasetURLS42		="http://downloads.dbpedia.org/2016-10/core-i18n/en/geo_coordinates_en.tql.bz2";
	protected static String datasetURLS43		="http://downloads.dbpedia.org/2016-10/core-i18n/en/geo_coordinates_en.ttl.bz2";
	protected static String datasetURLS44		="http://downloads.dbpedia.org/2016-10/core-i18n/en/geo_coordinates_mappingbased_en.tql.bz2";
	protected static String datasetURLS45		="http://downloads.dbpedia.org/2016-10/core-i18n/en/geo_coordinates_mappingbased_en.ttl.bz2";
	protected static String datasetURLS46		="http://downloads.dbpedia.org/2016-10/core-i18n/en/geo_coordinates_mappingbased_wkd_uris_en.tql.bz2";
	protected static String datasetURLS47		="http://downloads.dbpedia.org/2016-10/core-i18n/en/geo_coordinates_mappingbased_wkd_uris_en.ttl.bz2";
	protected static String datasetURLS48		="http://downloads.dbpedia.org/2016-10/core-i18n/en/geo_coordinates_wkd_uris_en.tql.bz2";
	protected static String datasetURLS49		="http://downloads.dbpedia.org/2016-10/core-i18n/en/geo_coordinates_wkd_uris_en.ttl.bz2";
	protected static String datasetURLS50		="http://downloads.dbpedia.org/2016-10/core-i18n/en/geonames_links_en.ttl.bz2";
	protected static String datasetURLS51		="http://downloads.dbpedia.org/2016-10/core-i18n/en/homepages_en.tql.bz2";
	protected static String datasetURLS52		="http://downloads.dbpedia.org/2016-10/core-i18n/en/homepages_en.ttl.bz2";
	protected static String datasetURLS53		="http://downloads.dbpedia.org/2016-10/core-i18n/en/homepages_wkd_uris_en.tql.bz2";
	protected static String datasetURLS54		="http://downloads.dbpedia.org/2016-10/core-i18n/en/homepages_wkd_uris_en.ttl.bz2";
	protected static String datasetURLS55		="http://downloads.dbpedia.org/2016-10/core-i18n/en/images_en.tql.bz2";
	protected static String datasetURLS56		="http://downloads.dbpedia.org/2016-10/core-i18n/en/images_en.ttl.bz2";
	protected static String datasetURLS57		="http://downloads.dbpedia.org/2016-10/core-i18n/en/images_wkd_uris_en.tql.bz2";
	protected static String datasetURLS58		="http://downloads.dbpedia.org/2016-10/core-i18n/en/images_wkd_uris_en.ttl.bz2";
	protected static String datasetURLS59		="http://downloads.dbpedia.org/2016-10/core-i18n/en/infobox_properties_en.tql.bz2";
	protected static String datasetURLS60		="http://downloads.dbpedia.org/2016-10/core-i18n/en/infobox_properties_en.ttl.bz2";
	protected static String datasetURLS61		="http://downloads.dbpedia.org/2016-10/core-i18n/en/infobox_properties_mapped_en.tql.bz2";
	protected static String datasetURLS62		="http://downloads.dbpedia.org/2016-10/core-i18n/en/infobox_properties_mapped_en.ttl.bz2";
	protected static String datasetURLS63		="http://downloads.dbpedia.org/2016-10/core-i18n/en/infobox_properties_sorted_en.ttl.bz2";
	protected static String datasetURLS64		="http://downloads.dbpedia.org/2016-10/core-i18n/en/infobox_properties_wkd_uris_en.tql.bz2";
	protected static String datasetURLS65		="http://downloads.dbpedia.org/2016-10/core-i18n/en/infobox_properties_wkd_uris_en.ttl.bz2";
	protected static String datasetURLS66		="http://downloads.dbpedia.org/2016-10/core-i18n/en/infobox_property_definitions_en.tql.bz2";
	protected static String datasetURLS67		="http://downloads.dbpedia.org/2016-10/core-i18n/en/infobox_property_definitions_en.ttl.bz2";
	protected static String datasetURLS68		="http://downloads.dbpedia.org/2016-10/core-i18n/en/infobox_property_definitions_wkd_uris_en.tql.bz2";
	protected static String datasetURLS69		="http://downloads.dbpedia.org/2016-10/core-i18n/en/infobox_property_definitions_wkd_uris_en.ttl.bz2";
	protected static String datasetURLS70		="http://downloads.dbpedia.org/2016-10/core-i18n/en/infobox_test_en.tql.bz2";
	protected static String datasetURLS71		="http://downloads.dbpedia.org/2016-10/core-i18n/en/infobox_test_en.ttl.bz2";
	protected static String datasetURLS72		="http://downloads.dbpedia.org/2016-10/core-i18n/en/instance_types_en.tql.bz2";
	protected static String datasetURLS73		="http://downloads.dbpedia.org/2016-10/core-i18n/en/instance_types_en.ttl.bz2";
	protected static String datasetURLS74		="http://downloads.dbpedia.org/2016-10/core-i18n/en/instance_types_lhd_dbo_en.ttl.bz2";
	protected static String datasetURLS75		="http://downloads.dbpedia.org/2016-10/core-i18n/en/instance_types_lhd_ext_en.ttl.bz2";
	protected static String datasetURLS76		="http://downloads.dbpedia.org/2016-10/core-i18n/en/instance_types_sdtyped_dbo_en.tql.bz2";
	protected static String datasetURLS77		="http://downloads.dbpedia.org/2016-10/core-i18n/en/instance_types_sdtyped_dbo_en.ttl.bz2";
	protected static String datasetURLS78		="http://downloads.dbpedia.org/2016-10/core-i18n/en/instance_types_sorted_en.ttl.bz2";
	protected static String datasetURLS79		="http://downloads.dbpedia.org/2016-10/core-i18n/en/instance_types_transitive_en.tql.bz2";
	protected static String datasetURLS80		="http://downloads.dbpedia.org/2016-10/core-i18n/en/instance_types_transitive_en.ttl.bz2";
	protected static String datasetURLS81		="http://downloads.dbpedia.org/2016-10/core-i18n/en/instance_types_transitive_wkd_uris_en.tql.bz2";
	protected static String datasetURLS82		="http://downloads.dbpedia.org/2016-10/core-i18n/en/instance_types_transitive_wkd_uris_en.ttl.bz2";
	protected static String datasetURLS83		="http://downloads.dbpedia.org/2016-10/core-i18n/en/instance_types_wkd_uris_en.tql.bz2";
	protected static String datasetURLS84		="http://downloads.dbpedia.org/2016-10/core-i18n/en/instance_types_wkd_uris_en.ttl.bz2";
	protected static String datasetURLS85		="http://downloads.dbpedia.org/2016-10/core-i18n/en/interlanguage_links_chapters_en.tql.bz2";
	protected static String datasetURLS86		="http://downloads.dbpedia.org/2016-10/core-i18n/en/interlanguage_links_chapters_en.ttl.bz2";
	protected static String datasetURLS87		="http://downloads.dbpedia.org/2016-10/core-i18n/en/interlanguage_links_en.tql.bz2";
	protected static String datasetURLS88		="http://downloads.dbpedia.org/2016-10/core-i18n/en/interlanguage_links_en.ttl.bz2";
	protected static String datasetURLS89		="http://downloads.dbpedia.org/2016-10/core-i18n/en/interlanguage_links_sorted_en.ttl.bz2";
	protected static String datasetURLS90		="http://downloads.dbpedia.org/2016-10/core-i18n/en/labels_en.tql.bz2";
	protected static String datasetURLS91		="http://downloads.dbpedia.org/2016-10/core-i18n/en/labels_en.ttl.bz2";
	protected static String datasetURLS92		="http://downloads.dbpedia.org/2016-10/core-i18n/en/labels_sorted_en.ttl.bz2";
	protected static String datasetURLS93		="http://downloads.dbpedia.org/2016-10/core-i18n/en/labels_wkd_uris_en.tql.bz2";
	protected static String datasetURLS94		="http://downloads.dbpedia.org/2016-10/core-i18n/en/labels_wkd_uris_en.ttl.bz2";
	protected static String datasetURLS95		="http://downloads.dbpedia.org/2016-10/core-i18n/en/lines-bytes-packed.csv";
	protected static String datasetURLS96		="http://downloads.dbpedia.org/2016-10/core-i18n/en/long_abstracts_en.tql.bz2";
	protected static String datasetURLS97		="http://downloads.dbpedia.org/2016-10/core-i18n/en/long_abstracts_en.ttl.bz2";
	protected static String datasetURLS98		="http://downloads.dbpedia.org/2016-10/core-i18n/en/long_abstracts_wkd_uris_en.tql.bz2";
	protected static String datasetURLS99		="http://downloads.dbpedia.org/2016-10/core-i18n/en/long_abstracts_wkd_uris_en.ttl.bz2";
	protected static String datasetURLS100		="http://downloads.dbpedia.org/2016-10/core-i18n/en/mappingbased_literals_en.tql.bz2";
	protected static String datasetURLS101		="http://downloads.dbpedia.org/2016-10/core-i18n/en/mappingbased_literals_en.ttl.bz2";
	protected static String datasetURLS102		="http://downloads.dbpedia.org/2016-10/core-i18n/en/mappingbased_literals_sorted_en.ttl.bz2";
	protected static String datasetURLS103		="http://downloads.dbpedia.org/2016-10/core-i18n/en/mappingbased_literals_wkd_uris_en.tql.bz2";
	protected static String datasetURLS104		="http://downloads.dbpedia.org/2016-10/core-i18n/en/mappingbased_literals_wkd_uris_en.ttl.bz2";
	protected static String datasetURLS105		="http://downloads.dbpedia.org/2016-10/core-i18n/en/mappingbased_objects_disjoint_domain_en.tql.bz2";
	protected static String datasetURLS106		="http://downloads.dbpedia.org/2016-10/core-i18n/en/mappingbased_objects_disjoint_domain_en.ttl.bz2";
	protected static String datasetURLS107		="http://downloads.dbpedia.org/2016-10/core-i18n/en/mappingbased_objects_disjoint_range_en.ttl.bz2";
	protected static String datasetURLS108		="http://downloads.dbpedia.org/2016-10/core-i18n/en/mappingbased_objects_disjoint_range_en.tql.bz2";
	protected static String datasetURLS109		="http://downloads.dbpedia.org/2016-10/core-i18n/en/mappingbased_objects_en.tql.bz2";
	protected static String datasetURLS110		="http://downloads.dbpedia.org/2016-10/core-i18n/en/mappingbased_objects_en.ttl.bz2";
	protected static String datasetURLS111		="http://downloads.dbpedia.org/2016-10/core-i18n/en/mappingbased_objects_uncleaned_en.tql.bz2";
	protected static String datasetURLS112		="http://downloads.dbpedia.org/2016-10/core-i18n/en/mappingbased_objects_uncleaned_en.ttl.bz2";
	protected static String datasetURLS113		="http://downloads.dbpedia.org/2016-10/core-i18n/en/mappingbased_objects_wkd_uris_en.tql.bz2";
	protected static String datasetURLS114		="http://downloads.dbpedia.org/2016-10/core-i18n/en/mappingbased_objects_wkd_uris_en.ttl.bz2";
	protected static String datasetURLS115		="http://downloads.dbpedia.org/2016-10/core-i18n/en/nif_context_en.tql.bz2";
	protected static String datasetURLS116		="http://downloads.dbpedia.org/2016-10/core-i18n/en/nif_context_en.ttl.bz2";
	protected static String datasetURLS117		="http://downloads.dbpedia.org/2016-10/core-i18n/en/nif_page_structure_en.tql.bz2";
	protected static String datasetURLS118		="http://downloads.dbpedia.org/2016-10/core-i18n/en/nif_page_structure_en.ttl.bz2";
	protected static String datasetURLS119		="http://downloads.dbpedia.org/2016-10/core-i18n/en/nif_text_links_en.tql.bz2";
	protected static String datasetURLS120		="http://downloads.dbpedia.org/2016-10/core-i18n/en/nif_text_links_en.ttl.bz2";
	protected static String datasetURLS121		="http://downloads.dbpedia.org/2016-10/core-i18n/en/out_degree_en.tql.bz2";
	protected static String datasetURLS122		="http://downloads.dbpedia.org/2016-10/core-i18n/en/out_degree_en.ttl.bz2";
	protected static String datasetURLS123		="http://downloads.dbpedia.org/2016-10/core-i18n/en/page_ids_en.tql.bz2";
	protected static String datasetURLS124		="http://downloads.dbpedia.org/2016-10/core-i18n/en/page_ids_en.ttl.bz2";
	protected static String datasetURLS125		="http://downloads.dbpedia.org/2016-10/core-i18n/en/page_ids_sorted_en.ttl.bz2";
	protected static String datasetURLS126		="http://downloads.dbpedia.org/2016-10/core-i18n/en/page_length_en.tql.bz2";
	protected static String datasetURLS127		="http://downloads.dbpedia.org/2016-10/core-i18n/en/page_length_en.ttl.bz2";
	protected static String datasetURLS128	    ="http://downloads.dbpedia.org/2016-10/core-i18n/en/page_links_en.tql.bz2";
	protected static String datasetURLS129	    ="http://downloads.dbpedia.org/2016-10/core-i18n/en/page_links_en.ttl.bz2";
	protected static String datasetURLS130	    ="http://downloads.dbpedia.org/2016-10/core-i18n/en/page_links_wkd_uris_en.tql.bz2";
	protected static String datasetURLS131		="http://downloads.dbpedia.org/2016-10/core-i18n/en/page_links_wkd_uris_en.ttl.bz2";
	protected static String datasetURLS132		="http://downloads.dbpedia.org/2016-10/core-i18n/en/persondata_en.tql.bz2";
	protected static String datasetURLS133		="http://downloads.dbpedia.org/2016-10/core-i18n/en/persondata_en.ttl.bz2";
	protected static String datasetURLS134		="http://downloads.dbpedia.org/2016-10/core-i18n/en/persondata_wkd_uris_en.tql.bz2";
	protected static String datasetURLS135		="http://downloads.dbpedia.org/2016-10/core-i18n/en/persondata_wkd_uris_en.ttl.bz2";
	protected static String datasetURLS136		="http://downloads.dbpedia.org/2016-10/core-i18n/en/pnd_en.tql.bz2";
	protected static String datasetURLS137		="http://downloads.dbpedia.org/2016-10/core-i18n/en/pnd_en.ttl.bz2";
	protected static String datasetURLS138		="http://downloads.dbpedia.org/2016-10/core-i18n/en/pnd_wkd_uris_en.tql.bz2";
	protected static String datasetURLS139		="http://downloads.dbpedia.org/2016-10/core-i18n/en/pnd_wkd_uris_en.ttl.bz2";
	protected static String datasetURLS140		="http://downloads.dbpedia.org/2016-10/core-i18n/en/raw_tables_en.tql.bz2";
	protected static String datasetURLS141		="http://downloads.dbpedia.org/2016-10/core-i18n/en/raw_tables_en.ttl.bz2";
	protected static String datasetURLS142		="http://downloads.dbpedia.org/2016-10/core-i18n/en/redirects_en.tql.bz2";
	protected static String datasetURLS143		="http://downloads.dbpedia.org/2016-10/core-i18n/en/redirects_en.ttl.bz2";
	protected static String datasetURLS144		="http://downloads.dbpedia.org/2016-10/core-i18n/en/revision_ids_en.tql.bz2";
	protected static String datasetURLS145		="http://downloads.dbpedia.org/2016-10/core-i18n/en/revision_ids_en.ttl.bz2";
	protected static String datasetURLS146		="http://downloads.dbpedia.org/2016-10/core-i18n/en/revision_uris_en.tql.bz2";
	protected static String datasetURLS147		="http://downloads.dbpedia.org/2016-10/core-i18n/en/revision_uris_en.ttl.bz2";
	protected static String datasetURLS148		="http://downloads.dbpedia.org/2016-10/core-i18n/en/short_abstracts_en.tql.bz2";
	protected static String datasetURLS149		="http://downloads.dbpedia.org/2016-10/core-i18n/en/short_abstracts_en.ttl.bz2";
	protected static String datasetURLS150		="http://downloads.dbpedia.org/2016-10/core-i18n/en/short_abstracts_sorted_en.ttl.bz2";
	protected static String datasetURLS151		="http://downloads.dbpedia.org/2016-10/core-i18n/en/short_abstracts_wkd_uris_en.tql.bz2";
	protected static String datasetURLS152		="http://downloads.dbpedia.org/2016-10/core-i18n/en/short_abstracts_wkd_uris_en.ttl.bz2";
	protected static String datasetURLS153		="http://downloads.dbpedia.org/2016-10/core-i18n/en/skos_categories_en.tql.bz2";
	protected static String datasetURLS154		="http://downloads.dbpedia.org/2016-10/core-i18n/en/skos_categories_en.ttl.bz2";
	protected static String datasetURLS155		="http://downloads.dbpedia.org/2016-10/core-i18n/en/skos_categories_wkd_uris_en.tql.bz2";
	protected static String datasetURLS156		="http://downloads.dbpedia.org/2016-10/core-i18n/en/skos_categories_wkd_uris_en.ttl.bz2";
	protected static String datasetURLS157		="http://downloads.dbpedia.org/2016-10/core-i18n/en/specific_mappingbased_properties_en.tql.bz2";
	protected static String datasetURLS158		="http://downloads.dbpedia.org/2016-10/core-i18n/en/specific_mappingbased_properties_en.ttl.bz2";
	protected static String datasetURLS159		="http://downloads.dbpedia.org/2016-10/core-i18n/en/specific_mappingbased_properties_wkd_uris_en.tql.bz2";
	protected static String datasetURLS160		="http://downloads.dbpedia.org/2016-10/core-i18n/en/specific_mappingbased_properties_wkd_uris_en.ttl.bz2";
	protected static String datasetURLS161		="http://downloads.dbpedia.org/2016-10/core-i18n/en/template_parameters_en.ttl.bz2";
	protected static String datasetURLS162		="http://downloads.dbpedia.org/2016-10/core-i18n/en/topical_concepts_en.tql.bz2";
	protected static String datasetURLS163		="http://downloads.dbpedia.org/2016-10/core-i18n/en/topical_concepts_en.ttl.bz2";
	protected static String datasetURLS164		="http://downloads.dbpedia.org/2016-10/core-i18n/en/topical_concepts_wkd_uris_en.tql.bz2";
	protected static String datasetURLS165		="http://downloads.dbpedia.org/2016-10/core-i18n/en/topical_concepts_wkd_uris_en.ttl.bz2";
	protected static String datasetURLS166		="http://downloads.dbpedia.org/2016-10/core-i18n/en/transitive_redirects_en.ttl.bz2";
	protected static String datasetURLS167		="http://downloads.dbpedia.org/2016-10/core-i18n/en/uri_same_as_iri_en.tql.bz2";
	protected static String datasetURLS168		="http://downloads.dbpedia.org/2016-10/core-i18n/en/uri_same_as_iri_en.ttl.bz2";
	protected static String datasetURLS169		="http://downloads.dbpedia.org/2016-10/core-i18n/en/wikipedia_links_en.tql.bz2";
	protected static String datasetURLS170		="http://downloads.dbpedia.org/2016-10/core-i18n/en/wikipedia_links_en.ttl.bz2";
	
	private static List list;
	private static TreeSet set;
	//private static ArrayList<String> words;
	
	
	
	
	/**
	 * @param datasetURLS1 the datasetURLS1 to set
	 */
	protected void setdatasetURLS1(String datasetURLS1) {
		this.datasetURLS1 = datasetURLS1;
	}
	/**
	 * @param datasetURLS2 the datasetURLS2 to set
	 */
	protected void setdatasetURLS2(String datasetURLS2) {
		this.datasetURLS2 = datasetURLS2;
	}
	/**
	 * @param datasetURLS3 the datasetURLS3 to set
	 */
	protected void setdatasetURLS3(String datasetURLS3) {
		this.datasetURLS3 = datasetURLS3;
	}
	/**
	 * @param datasetURLS4 the datasetURLS4 to set
	 */
	protected void setdatasetURLS4(String datasetURLS4) {
		this.datasetURLS4 = datasetURLS4;
	}
	/**
	 * @param datasetURLS5 the datasetURLS5 to set
	 */
	protected void setdatasetURLS5(String datasetURLS5) {
		this.datasetURLS5 = datasetURLS5;
	}
	/**
	 * @param datasetURLS6 the datasetURLS6 to set
	 */
	protected void setdatasetURLS6(String datasetURLS6) {
		this.datasetURLS6 = datasetURLS6;
	}
	/**
	 * @param datasetURLS7 the datasetURLS7 to set
	 */
	protected void setdatasetURLS7(String datasetURLS7) {
		this.datasetURLS7 = datasetURLS7;
	}
	/**
	 * @param datasetURLS8 the datasetURLS8 to set
	 */
	protected void setdatasetURLS8(String datasetURLS8) {
		this.datasetURLS8 = datasetURLS8;
	}
	/**
	 * @param datasetURLS9 the datasetURLS9 to set
	 */
	protected void setdatasetURLS9(String datasetURLS9) {
		this.datasetURLS9 = datasetURLS9;
	}
	/**
	 * @param datasetURLS10 the datasetURLS10 to set
	 */
	protected void setdatasetURLS10(String datasetURLS10) {
		this.datasetURLS10 = datasetURLS10;
	}
	/**
	 * @param datasetURLS11 the datasetURLS11 to set
	 */
	protected void setdatasetURLS11(String datasetURLS11) {
		this.datasetURLS11 = datasetURLS11;
	}
	/**
	 * @param datasetURLS12 the datasetURLS12 to set
	 */
	protected void setdatasetURLS12(String datasetURLS12) {
		this.datasetURLS12 = datasetURLS12;
	}
	/**
	 * @param datasetURLS13 the datasetURLS13 to set
	 */
	protected void setdatasetURLS13(String datasetURLS13) {
		this.datasetURLS13 = datasetURLS13;
	}
	/**
	 * @param datasetURLS14 the datasetURLS14 to set
	 */
	protected void setdatasetURLS14(String datasetURLS14) {
		this.datasetURLS14 = datasetURLS14;
	}
	/**
	 * @param datasetURLS15 the datasetURLS15 to set
	 */
	protected void setdatasetURLS15(String datasetURLS15) {
		this.datasetURLS15 = datasetURLS15;
	}
	/**
	 * @param datasetURLS16 the datasetURLS16 to set
	 */
	protected void setdatasetURLS16(String datasetURLS16) {
		this.datasetURLS16 = datasetURLS16;
	}
	/**
	 * @param datasetURLS17 the datasetURLS17 to set
	 */
	protected void setdatasetURLS17(String datasetURLS17) {
		this.datasetURLS17 = datasetURLS17;
	}
	/**
	 * @param datasetURLS18 the datasetURLS18 to set
	 */
	protected void setdatasetURLS18(String datasetURLS18) {
		this.datasetURLS18 = datasetURLS18;
	}
	/**
	 * @param datasetURLS19 the datasetURLS19 to set
	 */
	protected void setdatasetURLS19(String datasetURLS19) {
		this.datasetURLS19 = datasetURLS19;
	}
	/**
	 * @param datasetURLS20 the datasetURLS20 to set
	 */
	protected void setdatasetURLS20(String datasetURLS20) {
		this.datasetURLS20 = datasetURLS20;
	}
	/**
	 * @param datasetURLS21 the datasetURLS21 to set
	 */
	protected void setdatasetURLS21(String datasetURLS21) {
		this.datasetURLS21 = datasetURLS21;
	}
	/**
	 * @param datasetURLS22 the datasetURLS22 to set
	 */
	protected void setdatasetURLS22(String datasetURLS22) {
		this.datasetURLS22 = datasetURLS22;
	}
	/**
	 * @param datasetURLS23 the datasetURLS23 to set
	 */
	protected void setdatasetURLS23(String datasetURLS23) {
		this.datasetURLS23 = datasetURLS23;
	}
	/**
	 * @param datasetURLS24 the datasetURLS24 to set
	 */
	protected void setdatasetURLS24(String datasetURLS24) {
		this.datasetURLS24 = datasetURLS24;
	}
	/**
	 * @param datasetURLS25 the datasetURLS25 to set
	 */
	protected void setdatasetURLS25(String datasetURLS25) {
		this.datasetURLS25 = datasetURLS25;
	}
	/**
	 * @param datasetURLS26 the datasetURLS26 to set
	 */
	protected void setdatasetURLS26(String datasetURLS26) {
		this.datasetURLS26 = datasetURLS26;
	}
	/**
	 * @param datasetURLS27 the datasetURLS27 to set
	 */
	protected void setdatasetURLS27(String datasetURLS27) {
		this.datasetURLS27 = datasetURLS27;
	}
	/**
	 * @param datasetURLS28 the datasetURLS28 to set
	 */
	protected void setdatasetURLS28(String datasetURLS28) {
		this.datasetURLS28 = datasetURLS28;
	}
	/**
	 * @param datasetURLS29 the datasetURLS29 to set
	 */
	protected void setdatasetURLS29(String datasetURLS29) {
		this.datasetURLS29 = datasetURLS29;
	}
	/**
	 * @param datasetURLS30 the datasetURLS30 to set
	 */
	protected void setdatasetURLS30(String datasetURLS30) {
		this.datasetURLS30 = datasetURLS30;
	}
	/**
	 * @param datasetURLS31 the datasetURLS31 to set
	 */
	protected void setdatasetURLS31(String datasetURLS31) {
		this.datasetURLS31 = datasetURLS31;
	}
	/**
	 * @param datasetURLS32 the datasetURLS32 to set
	 */
	protected void setdatasetURLS32(String datasetURLS32) {
		this.datasetURLS32 = datasetURLS32;
	}
	/**
	 * @param datasetURLS33 the datasetURLS33 to set
	 */
	protected void setdatasetURLS33(String datasetURLS33) {
		this.datasetURLS33 = datasetURLS33;
	}
	/**
	 * @param datasetURLS34 the datasetURLS34 to set
	 */
	protected void setdatasetURLS34(String datasetURLS34) {
		this.datasetURLS34 = datasetURLS34;
	}
	/**
	 * @param datasetURLS35 the datasetURLS35 to set
	 */
	protected void setdatasetURLS35(String datasetURLS35) {
		this.datasetURLS35 = datasetURLS35;
	}
	/**
	 * @param datasetURLS36 the datasetURLS36 to set
	 */
	protected void setdatasetURLS36(String datasetURLS36) {
		this.datasetURLS36 = datasetURLS36;
	}
	/**
	 * @param datasetURLS37 the datasetURLS37 to set
	 */
	protected void setdatasetURLS37(String datasetURLS37) {
		this.datasetURLS37 = datasetURLS37;
	}
	/**
	 * @param datasetURLS38 the datasetURLS38 to set
	 */
	protected void setdatasetURLS38(String datasetURLS38) {
		this.datasetURLS38 = datasetURLS38;
	}
	/**
	 * @param datasetURLS39 the datasetURLS39 to set
	 */
	protected void setdatasetURLS39(String datasetURLS39) {
		this.datasetURLS39 = datasetURLS39;
	}
	/**
	 * @param datasetURLS40 the datasetURLS40 to set
	 */
	protected void setdatasetURLS40(String datasetURLS40) {
		this.datasetURLS40 = datasetURLS40;
	}
	/**
	 * @param datasetURLS41 the datasetURLS41 to set
	 */
	protected void setdatasetURLS41(String datasetURLS41) {
		this.datasetURLS41 = datasetURLS41;
	}
	/**
	 * @param datasetURLS42 the datasetURLS42 to set
	 */
	protected void setdatasetURLS42(String datasetURLS42) {
		this.datasetURLS42 = datasetURLS42;
	}
	/**
	 * @param datasetURLS43 the datasetURLS43 to set
	 */
	protected void setdatasetURLS43(String datasetURLS43) {
		this.datasetURLS43 = datasetURLS43;
	}
	/**
	 * @param datasetURLS44 the datasetURLS44 to set
	 */
	protected void setdatasetURLS44(String datasetURLS44) {
		this.datasetURLS44 = datasetURLS44;
	}
	/**
	 * @param datasetURLS45 the datasetURLS45 to set
	 */
	protected void setdatasetURLS45(String datasetURLS45) {
		this.datasetURLS45 = datasetURLS45;
	}
	/**
	 * @param datasetURLS46 the datasetURLS46 to set
	 */
	protected void setdatasetURLS46(String datasetURLS46) {
		this.datasetURLS46 = datasetURLS46;
	}
	/**
	 * @param datasetURLS47 the datasetURLS47 to set
	 */
	protected void setdatasetURLS47(String datasetURLS47) {
		this.datasetURLS47 = datasetURLS47;
	}
	/**
	 * @param datasetURLS48 the datasetURLS48 to set
	 */
	protected void setdatasetURLS48(String datasetURLS48) {
		this.datasetURLS48 = datasetURLS48;
	}
	/**
	 * @param datasetURLS49 the datasetURLS49 to set
	 */
	protected void setdatasetURLS49(String datasetURLS49) {
		this.datasetURLS49 = datasetURLS49;
	}
	/**
	 * @param datasetURLS50 the datasetURLS50 to set
	 */
	protected void setdatasetURLS50(String datasetURLS50) {
		this.datasetURLS50 = datasetURLS50;
	}
	/**
	 * @param datasetURLS51 the datasetURLS51 to set
	 */
	protected void setdatasetURLS51(String datasetURLS51) {
		this.datasetURLS51 = datasetURLS51;
	}
	/**
	 * @param datasetURLS52 the datasetURLS52 to set
	 */
	protected void setdatasetURLS52(String datasetURLS52) {
		this.datasetURLS52 = datasetURLS52;
	}
	/**
	 * @param datasetURLS53 the datasetURLS53 to set
	 */
	protected void setdatasetURLS53(String datasetURLS53) {
		this.datasetURLS53 = datasetURLS53;
	}
	/**
	 * @param datasetURLS54 the datasetURLS54 to set
	 */
	protected void setdatasetURLS54(String datasetURLS54) {
		this.datasetURLS54 = datasetURLS54;
	}
	/**
	 * @param datasetURLS55 the datasetURLS55 to set
	 */
	protected void setdatasetURLS55(String datasetURLS55) {
		this.datasetURLS55 = datasetURLS55;
	}
	/**
	 * @param datasetURLS56 the datasetURLS56 to set
	 */
	protected void setdatasetURLS56(String datasetURLS56) {
		this.datasetURLS56 = datasetURLS56;
	}
	/**
	 * @param datasetURLS57 the datasetURLS57 to set
	 */
	protected void setdatasetURLS57(String datasetURLS57) {
		this.datasetURLS57 = datasetURLS57;
	}
	/**
	 * @param datasetURLS58 the datasetURLS58 to set
	 */
	protected void setdatasetURLS58(String datasetURLS58) {
		this.datasetURLS58 = datasetURLS58;
	}
	/**
	 * @param datasetURLS59 the datasetURLS59 to set
	 */
	protected void setdatasetURLS59(String datasetURLS59) {
		this.datasetURLS59 = datasetURLS59;
	}
	/**
	 * @param datasetURLS60 the datasetURLS60 to set
	 */
	protected void setdatasetURLS60(String datasetURLS60) {
		this.datasetURLS60 = datasetURLS60;
	}
	/**
	 * @param datasetURLS61 the datasetURLS61 to set
	 */
	protected void setdatasetURLS61(String datasetURLS61) {
		this.datasetURLS61 = datasetURLS61;
	}
	/**
	 * @param datasetURLS62 the datasetURLS62 to set
	 */
	protected void setdatasetURLS62(String datasetURLS62) {
		this.datasetURLS62 = datasetURLS62;
	}
	/**
	 * @param datasetURLS63 the datasetURLS63 to set
	 */
	protected void setdatasetURLS63(String datasetURLS63) {
		this.datasetURLS63 = datasetURLS63;
	}
	/**
	 * @param datasetURLS64 the datasetURLS64 to set
	 */
	protected void setdatasetURLS64(String datasetURLS64) {
		this.datasetURLS64 = datasetURLS64;
	}
	/**
	 * @param datasetURLS65 the datasetURLS65 to set
	 */
	protected void setdatasetURLS65(String datasetURLS65) {
		this.datasetURLS65 = datasetURLS65;
	}
	/**
	 * @param datasetURLS66 the datasetURLS66 to set
	 */
	protected void setdatasetURLS66(String datasetURLS66) {
		this.datasetURLS66 = datasetURLS66;
	}
	/**
	 * @param datasetURLS67 the datasetURLS67 to set
	 */
	protected void setdatasetURLS67(String datasetURLS67) {
		this.datasetURLS67 = datasetURLS67;
	}
	/**
	 * @param datasetURLS68 the datasetURLS68 to set
	 */
	protected void setdatasetURLS68(String datasetURLS68) {
		this.datasetURLS68 = datasetURLS68;
	}
	/**
	 * @param datasetURLS69 the datasetURLS69 to set
	 */
	protected void setdatasetURLS69(String datasetURLS69) {
		this.datasetURLS69 = datasetURLS69;
	}
	/**
	 * @param datasetURLS70 the datasetURLS70 to set
	 */
	protected void setdatasetURLS70(String datasetURLS70) {
		this.datasetURLS70 = datasetURLS70;
	}
	/**
	 * @param datasetURLS71 the datasetURLS71 to set
	 */
	protected void setdatasetURLS71(String datasetURLS71) {
		this.datasetURLS71 = datasetURLS71;
	}
	/**
	 * @param datasetURLS72 the datasetURLS72 to set
	 */
	protected void setdatasetURLS72(String datasetURLS72) {
		this.datasetURLS72 = datasetURLS72;
	}
	/**
	 * @param datasetURLS73 the datasetURLS73 to set
	 */
	protected void setdatasetURLS73(String datasetURLS73) {
		this.datasetURLS73 = datasetURLS73;
	}
	/**
	 * @param datasetURLS74 the datasetURLS74 to set
	 */
	protected void setdatasetURLS74(String datasetURLS74) {
		this.datasetURLS74 = datasetURLS74;
	}
	/**
	 * @param datasetURLS75 the datasetURLS75 to set
	 */
	protected void setdatasetURLS75(String datasetURLS75) {
		this.datasetURLS75 = datasetURLS75;
	}
	/**
	 * @param datasetURLS76 the datasetURLS76 to set
	 */
	protected void setdatasetURLS76(String datasetURLS76) {
		this.datasetURLS76 = datasetURLS76;
	}
	/**
	 * @param datasetURLS77 the datasetURLS77 to set
	 */
	protected void setdatasetURLS77(String datasetURLS77) {
		this.datasetURLS77 = datasetURLS77;
	}
	/**
	 * @param datasetURLS78 the datasetURLS78 to set
	 */
	protected void setdatasetURLS78(String datasetURLS78) {
		this.datasetURLS78 = datasetURLS78;
	}
	/**
	 * @param datasetURLS79 the datasetURLS79 to set
	 */
	protected void setdatasetURLS79(String datasetURLS79) {
		this.datasetURLS79 = datasetURLS79;
	}
	/**
	 * @param datasetURLS80 the datasetURLS80 to set
	 */
	protected void setdatasetURLS80(String datasetURLS80) {
		this.datasetURLS80 = datasetURLS80;
	}
	/**
	 * @param datasetURLS81 the datasetURLS81 to set
	 */
	protected void setdatasetURLS81(String datasetURLS81) {
		this.datasetURLS81 = datasetURLS81;
	}
	/**
	 * @param datasetURLS82 the datasetURLS82 to set
	 */
	protected void setdatasetURLS82(String datasetURLS82) {
		this.datasetURLS82 = datasetURLS82;
	}
	/**
	 * @param datasetURLS83 the datasetURLS83 to set
	 */
	protected void setdatasetURLS83(String datasetURLS83) {
		this.datasetURLS83 = datasetURLS83;
	}
	/**
	 * @param datasetURLS84 the datasetURLS84 to set
	 */
	protected void setdatasetURLS84(String datasetURLS84) {
		this.datasetURLS84 = datasetURLS84;
	}
	/**
	 * @param datasetURLS85 the datasetURLS85 to set
	 */
	protected void setdatasetURLS85(String datasetURLS85) {
		this.datasetURLS85 = datasetURLS85;
	}
	/**
	 * @param datasetURLS86 the datasetURLS86 to set
	 */
	protected void setdatasetURLS86(String datasetURLS86) {
		this.datasetURLS86 = datasetURLS86;
	}
	/**
	 * @param datasetURLS87 the datasetURLS87 to set
	 */
	protected void setdatasetURLS87(String datasetURLS87) {
		this.datasetURLS87 = datasetURLS87;
	}
	/**
	 * @param datasetURLS88 the datasetURLS88 to set
	 */
	protected void setdatasetURLS88(String datasetURLS88) {
		this.datasetURLS88 = datasetURLS88;
	}
	/**
	 * @param datasetURLS89 the datasetURLS89 to set
	 */
	protected void setdatasetURLS89(String datasetURLS89) {
		this.datasetURLS89 = datasetURLS89;
	}
	/**
	 * @param datasetURLS90 the datasetURLS90 to set
	 */
	protected void setdatasetURLS90(String datasetURLS90) {
		this.datasetURLS90 = datasetURLS90;
	}
	/**
	 * @param datasetURLS91 the datasetURLS91 to set
	 */
	protected void setdatasetURLS91(String datasetURLS91) {
		this.datasetURLS91 = datasetURLS91;
	}
	/**
	 * @param datasetURLS92 the datasetURLS92 to set
	 */
	protected void setdatasetURLS92(String datasetURLS92) {
		this.datasetURLS92 = datasetURLS92;
	}
	/**
	 * @param datasetURLS93 the datasetURLS93 to set
	 */
	protected void setdatasetURLS93(String datasetURLS93) {
		this.datasetURLS93 = datasetURLS93;
	}
	/**
	 * @param datasetURLS94 the datasetURLS94 to set
	 */
	protected void setdatasetURLS94(String datasetURLS94) {
		this.datasetURLS94 = datasetURLS94;
	}
	/**
	 * @param datasetURLS95 the datasetURLS95 to set
	 */
	protected void setdatasetURLS95(String datasetURLS95) {
		this.datasetURLS95 = datasetURLS95;
	}
	/**
	 * @param datasetURLS96 the datasetURLS96 to set
	 */
	protected void setdatasetURLS96(String datasetURLS96) {
		this.datasetURLS96 = datasetURLS96;
	}
	/**
	 * @param datasetURLS97 the datasetURLS97 to set
	 */
	protected void setdatasetURLS97(String datasetURLS97) {
		this.datasetURLS97 = datasetURLS97;
	}
	/**
	 * @param datasetURLS98 the datasetURLS98 to set
	 */
	protected void setdatasetURLS98(String datasetURLS98) {
		this.datasetURLS98 = datasetURLS98;
	}
	/**
	 * @param datasetURLS99 the datasetURLS99 to set
	 */
	protected void setdatasetURLS99(String datasetURLS99) {
		this.datasetURLS99 = datasetURLS99;
	}
	/**
	 * @param datasetURLS100 the datasetURLS100 to set
	 */
	protected void setdatasetURLS100(String datasetURLS100) {
		this.datasetURLS100 = datasetURLS100;
	}
	/**
	 * @param datasetURLS101 the datasetURLS101 to set
	 */
	protected void setdatasetURLS101(String datasetURLS101) {
		this.datasetURLS101 = datasetURLS101;
	}
	/**
	 * @param datasetURLS102 the datasetURLS102 to set
	 */
	protected void setdatasetURLS102(String datasetURLS102) {
		this.datasetURLS102 = datasetURLS102;
	}
	/**
	 * @param datasetURLS103 the datasetURLS103 to set
	 */
	protected void setdatasetURLS103(String datasetURLS103) {
		this.datasetURLS103 = datasetURLS103;
	}
	/**
	 * @param datasetURLS104 the datasetURLS104 to set
	 */
	protected void setdatasetURLS104(String datasetURLS104) {
		this.datasetURLS104 = datasetURLS104;
	}
	/**
	 * @param datasetURLS105 the datasetURLS105 to set
	 */
	protected void setdatasetURLS105(String datasetURLS105) {
		this.datasetURLS105 = datasetURLS105;
	}
	/**
	 * @param datasetURLS106 the datasetURLS106 to set
	 */
	protected void setdatasetURLS106(String datasetURLS106) {
		this.datasetURLS106 = datasetURLS106;
	}
	/**
	 * @param datasetURLS107 the datasetURLS107 to set
	 */
	protected void setdatasetURLS107(String datasetURLS107) {
		this.datasetURLS107 = datasetURLS107;
	}
	/**
	 * @param datasetURLS108 the datasetURLS108 to set
	 */
	protected void setdatasetURLS108(String datasetURLS108) {
		this.datasetURLS108 = datasetURLS108;
	}
	/**
	 * @param datasetURLS109 the datasetURLS109 to set
	 */
	protected void setdatasetURLS109(String datasetURLS109) {
		this.datasetURLS109 = datasetURLS109;
	}
	/**
	 * @param datasetURLS110 the datasetURLS110 to set
	 */
	protected void setdatasetURLS110(String datasetURLS110) {
		this.datasetURLS110 = datasetURLS110;
	}
	/**
	 * @param datasetURLS111 the datasetURLS111 to set
	 */
	protected void setdatasetURLS111(String datasetURLS111) {
		this.datasetURLS111 = datasetURLS111;
	}
	/**
	 * @param datasetURLS112 the datasetURLS112 to set
	 */
	protected void setdatasetURLS112(String datasetURLS112) {
		this.datasetURLS112 = datasetURLS112;
	}
	/**
	 * @param datasetURLS113 the datasetURLS113 to set
	 */
	protected void setdatasetURLS113(String datasetURLS113) {
		this.datasetURLS113 = datasetURLS113;
	}
	/**
	 * @param datasetURLS114 the datasetURLS114 to set
	 */
	protected void setdatasetURLS114(String datasetURLS114) {
		this.datasetURLS114 = datasetURLS114;
	}
	/**
	 * @param datasetURLS115 the datasetURLS115 to set
	 */
	protected void setdatasetURLS115(String datasetURLS115) {
		this.datasetURLS115 = datasetURLS115;
	}
	/**
	 * @param datasetURLS116 the datasetURLS116 to set
	 */
	protected void setdatasetURLS116(String datasetURLS116) {
		this.datasetURLS116 = datasetURLS116;
	}
	/**
	 * @param datasetURLS117 the datasetURLS117 to set
	 */
	protected void setdatasetURLS117(String datasetURLS117) {
		this.datasetURLS117 = datasetURLS117;
	}
	/**
	 * @param datasetURLS118 the datasetURLS118 to set
	 */
	protected void setdatasetURLS118(String datasetURLS118) {
		this.datasetURLS118 = datasetURLS118;
	}
	/**
	 * @param datasetURLS119 the datasetURLS119 to set
	 */
	protected void setdatasetURLS119(String datasetURLS119) {
		this.datasetURLS119 = datasetURLS119;
	}
	/**
	 * @param datasetURLS120 the datasetURLS120 to set
	 */
	protected void setdatasetURLS120(String datasetURLS120) {
		this.datasetURLS120 = datasetURLS120;
	}
	/**
	 * @param datasetURLS121 the datasetURLS121 to set
	 */
	protected void setdatasetURLS121(String datasetURLS121) {
		this.datasetURLS121 = datasetURLS121;
	}
	/**
	 * @param datasetURLS122 the datasetURLS122 to set
	 */
	protected void setdatasetURLS122(String datasetURLS122) {
		this.datasetURLS122 = datasetURLS122;
	}
	/**
	 * @param datasetURLS123 the datasetURLS123 to set
	 */
	protected void setdatasetURLS123(String datasetURLS123) {
		this.datasetURLS123 = datasetURLS123;
	}
	/**
	 * @param datasetURLS124 the datasetURLS124 to set
	 */
	protected void setdatasetURLS124(String datasetURLS124) {
		this.datasetURLS124 = datasetURLS124;
	}
	/**
	 * @param datasetURLS125 the datasetURLS125 to set
	 */
	protected void setdatasetURLS125(String datasetURLS125) {
		this.datasetURLS125 = datasetURLS125;
	}
	/**
	 * @param datasetURLS126 the datasetURLS126 to set
	 */
	protected void setdatasetURLS126(String datasetURLS126) {
		this.datasetURLS126 = datasetURLS126;
	}
	/**
	 * @param datasetURLS127 the datasetURLS127 to set
	 */
	protected void setdatasetURLS127(String datasetURLS127) {
		this.datasetURLS127 = datasetURLS127;
	}
	/**
	 * @param datasetURLS128 the datasetURLS128 to set
	 */
	protected void setdatasetURLS128(String datasetURLS128) {
		this.datasetURLS128 = datasetURLS128;
	}
	/**
	 * @param datasetURLS129 the datasetURLS129 to set
	 */
	protected void setdatasetURLS129(String datasetURLS129) {
		this.datasetURLS129 = datasetURLS129;
	}
	/**
	 * @param datasetURLS130 the datasetURLS130 to set
	 */
	protected void setdatasetURLS130(String datasetURLS130) {
		this.datasetURLS130 = datasetURLS130;
	}
	/**
	 * @param datasetURLS131 the datasetURLS131 to set
	 */
	protected void setdatasetURLS131(String datasetURLS131) {
		this.datasetURLS131 = datasetURLS131;
	}
	/**
	 * @param datasetURLS132 the datasetURLS132 to set
	 */
	protected void setdatasetURLS132(String datasetURLS132) {
		this.datasetURLS132 = datasetURLS132;
	}
	/**
	 * @param datasetURLS133 the datasetURLS133 to set
	 */
	protected void setdatasetURLS133(String datasetURLS133) {
		this.datasetURLS133 = datasetURLS133;
	}
	/**
	 * @param datasetURLS134 the datasetURLS134 to set
	 */
	protected void setdatasetURLS134(String datasetURLS134) {
		this.datasetURLS134 = datasetURLS134;
	}
	/**
	 * @param datasetURLS135 the datasetURLS135 to set
	 */
	protected void setdatasetURLS135(String datasetURLS135) {
		this.datasetURLS135 = datasetURLS135;
	}
	/**
	 * @param datasetURLS136 the datasetURLS136 to set
	 */
	protected void setdatasetURLS136(String datasetURLS136) {
		this.datasetURLS136 = datasetURLS136;
	}
	/**
	 * @param datasetURLS137 the datasetURLS137 to set
	 */
	protected void setdatasetURLS137(String datasetURLS137) {
		this.datasetURLS137 = datasetURLS137;
	}
	/**
	 * @param datasetURLS138 the datasetURLS138 to set
	 */
	protected void setdatasetURLS138(String datasetURLS138) {
		this.datasetURLS138 = datasetURLS138;
	}
	/**
	 * @param datasetURLS139 the datasetURLS139 to set
	 */
	protected void setdatasetURLS139(String datasetURLS139) {
		this.datasetURLS139 = datasetURLS139;
	}
	/**
	 * @param datasetURLS140 the datasetURLS140 to set
	 */
	protected void setdatasetURLS140(String datasetURLS140) {
		this.datasetURLS140 = datasetURLS140;
	}
	/**
	 * @param datasetURLS141 the datasetURLS141 to set
	 */
	protected void setdatasetURLS141(String datasetURLS141) {
		this.datasetURLS141 = datasetURLS141;
	}
	/**
	 * @param datasetURLS142 the datasetURLS142 to set
	 */
	protected void setdatasetURLS142(String datasetURLS142) {
		this.datasetURLS142 = datasetURLS142;
	}
	/**
	 * @param datasetURLS143 the datasetURLS143 to set
	 */
	protected void setdatasetURLS143(String datasetURLS143) {
		this.datasetURLS143 = datasetURLS143;
	}
	/**
	 * @param datasetURLS144 the datasetURLS144 to set
	 */
	protected void setdatasetURLS144(String datasetURLS144) {
		this.datasetURLS144 = datasetURLS144;
	}
	/**
	 * @param datasetURLS145 the datasetURLS145 to set
	 */
	protected void setdatasetURLS145(String datasetURLS145) {
		this.datasetURLS145 = datasetURLS145;
	}
	/**
	 * @param datasetURLS146 the datasetURLS146 to set
	 */
	protected void setdatasetURLS146(String datasetURLS146) {
		this.datasetURLS146 = datasetURLS146;
	}
	/**
	 * @param datasetURLS147 the datasetURLS147 to set
	 */
	protected void setdatasetURLS147(String datasetURLS147) {
		this.datasetURLS147 = datasetURLS147;
	}
	/**
	 * @param datasetURLS148 the datasetURLS148 to set
	 */
	protected void setdatasetURLS148(String datasetURLS148) {
		this.datasetURLS148 = datasetURLS148;
	}
	/**
	 * @param datasetURLS149 the datasetURLS149 to set
	 */
	protected void setdatasetURLS149(String datasetURLS149) {
		this.datasetURLS149 = datasetURLS149;
	}
	/**
	 * @param datasetURLS150 the datasetURLS150 to set
	 */
	protected void setdatasetURLS150(String datasetURLS150) {
		this.datasetURLS150 = datasetURLS150;
	}
	/**
	 * @param datasetURLS151 the datasetURLS151 to set
	 */
	protected void setdatasetURLS151(String datasetURLS151) {
		this.datasetURLS151 = datasetURLS151;
	}
	/**
	 * @param datasetURLS152 the datasetURLS152 to set
	 */
	protected void setdatasetURLS152(String datasetURLS152) {
		this.datasetURLS152 = datasetURLS152;
	}
	/**
	 * @param datasetURLS153 the datasetURLS153 to set
	 */
	protected void setdatasetURLS153(String datasetURLS153) {
		this.datasetURLS153 = datasetURLS153;
	}
	/**
	 * @param datasetURLS154 the datasetURLS154 to set
	 */
	protected void setdatasetURLS154(String datasetURLS154) {
		this.datasetURLS154 = datasetURLS154;
	}
	/**
	 * @param datasetURLS155 the datasetURLS155 to set
	 */
	protected void setdatasetURLS155(String datasetURLS155) {
		this.datasetURLS155 = datasetURLS155;
	}
	/**
	 * @param datasetURLS156 the datasetURLS156 to set
	 */
	protected void setdatasetURLS156(String datasetURLS156) {
		this.datasetURLS156 = datasetURLS156;
	}
	/**
	 * @param datasetURLS157 the datasetURLS157 to set
	 */
	protected void setdatasetURLS157(String datasetURLS157) {
		this.datasetURLS157 = datasetURLS157;
	}
	/**
	 * @param datasetURLS158 the datasetURLS158 to set
	 */
	protected void setdatasetURLS158(String datasetURLS158) {
		this.datasetURLS158 = datasetURLS158;
	}
	/**
	 * @param datasetURLS159 the datasetURLS159 to set
	 */
	protected void setdatasetURLS159(String datasetURLS159) {
		this.datasetURLS159 = datasetURLS159;
	}
	/**
	 * @param datasetURLS160 the datasetURLS160 to set
	 */
	protected void setdatasetURLS160(String datasetURLS160) {
		this.datasetURLS160 = datasetURLS160;
	}
	/**
	 * @param datasetURLS161 the datasetURLS161 to set
	 */
	protected void setdatasetURLS161(String datasetURLS161) {
		this.datasetURLS161 = datasetURLS161;
	}
	/**
	 * @param datasetURLS162 the datasetURLS162 to set
	 */
	protected void setdatasetURLS162(String datasetURLS162) {
		this.datasetURLS162 = datasetURLS162;
	}
	/**
	 * @param datasetURLS163 the datasetURLS163 to set
	 */
	protected void setdatasetURLS163(String datasetURLS163) {
		this.datasetURLS163 = datasetURLS163;
	}
	/**
	 * @param datasetURLS164 the datasetURLS164 to set
	 */
	protected void setdatasetURLS164(String datasetURLS164) {
		this.datasetURLS164 = datasetURLS164;
	}
	/**
	 * @param datasetURLS165 the datasetURLS165 to set
	 */
	protected void setdatasetURLS165(String datasetURLS165) {
		this.datasetURLS165 = datasetURLS165;
	}
	/**
	 * @param datasetURLS166 the datasetURLS166 to set
	 */
	protected void setdatasetURLS166(String datasetURLS166) {
		this.datasetURLS166 = datasetURLS166;
	}
	/**
	 * @param datasetURLS167 the datasetURLS167 to set
	 */
	protected void setdatasetURLS167(String datasetURLS167) {
		this.datasetURLS167 = datasetURLS167;
	}
	/**
	 * @param datasetURLS168 the datasetURLS168 to set
	 */
	protected void setdatasetURLS168(String datasetURLS168) {
		this.datasetURLS168 = datasetURLS168;
	}
	/**
	 * @param datasetURLS169 the datasetURLS169 to set
	 */
	protected void setdatasetURLS169(String datasetURLS169) {
		this.datasetURLS169 = datasetURLS169;
	}
	/**
	 * @param datasetURLS170 the datasetURLS170 to set
	 */
	protected void setdatasetURLS170(String datasetURLS170) {
		this.datasetURLS170 = datasetURLS170;
	}
	
	
	
	public  static TreeSet listMethod() {
		
		int i=0;
		
		 list = new ArrayList();
		 set = new TreeSet<>();
		for(i=0;i<170;i++)
		{
			
			list.add(datasetURLS1);
			list.add(datasetURLS2);
			list.add(datasetURLS3);
			list.add(datasetURLS4);
			list.add(datasetURLS5);
			list.add(datasetURLS6);
			list.add(datasetURLS7);
			list.add(datasetURLS8);
			list.add(datasetURLS9);
			list.add(datasetURLS10);
			list.add(datasetURLS11);
			list.add(datasetURLS12);
			list.add(datasetURLS13);
			list.add(datasetURLS14);
			list.add(datasetURLS15);
			list.add(datasetURLS16);
			list.add(datasetURLS17);
			list.add(datasetURLS18);
			list.add(datasetURLS19);
			list.add(datasetURLS20);
			list.add(datasetURLS21);
			list.add(datasetURLS22);
			list.add(datasetURLS23);
			list.add(datasetURLS24);
			list.add(datasetURLS25);
			list.add(datasetURLS26);
			list.add(datasetURLS27);
			list.add(datasetURLS28);
			list.add(datasetURLS29);
			list.add(datasetURLS30);
			list.add(datasetURLS31);
			list.add(datasetURLS32);
			list.add(datasetURLS33);
			list.add(datasetURLS34);
			list.add(datasetURLS35);
			list.add(datasetURLS36);
			list.add(datasetURLS37);
			list.add(datasetURLS38);
			list.add(datasetURLS39);
			list.add(datasetURLS40);
			list.add(datasetURLS41);
			list.add(datasetURLS42);
			list.add(datasetURLS43);
			list.add(datasetURLS44);
			list.add(datasetURLS45);
			list.add(datasetURLS46);
			list.add(datasetURLS47);
			list.add(datasetURLS48);
			list.add(datasetURLS49);
			list.add(datasetURLS50);
			list.add(datasetURLS51);
			list.add(datasetURLS52);
			list.add(datasetURLS53);
			list.add(datasetURLS54);
			list.add(datasetURLS55);
			list.add(datasetURLS56);
			list.add(datasetURLS57);
			list.add(datasetURLS58);
			list.add(datasetURLS59);
			list.add(datasetURLS60);
			list.add(datasetURLS61);
			list.add(datasetURLS62);
			list.add(datasetURLS63);
			list.add(datasetURLS64);
			list.add(datasetURLS65);
			list.add(datasetURLS66);
			list.add(datasetURLS67);
			list.add(datasetURLS68);
			list.add(datasetURLS69);
			list.add(datasetURLS70);
			list.add(datasetURLS71);
			list.add(datasetURLS72);
			list.add(datasetURLS73);
			list.add(datasetURLS74);
			list.add(datasetURLS75);
			list.add(datasetURLS76);
			list.add(datasetURLS77);
			list.add(datasetURLS78);
			list.add(datasetURLS79);
			list.add(datasetURLS80);
			list.add(datasetURLS81);
			list.add(datasetURLS82);
			list.add(datasetURLS83);
			list.add(datasetURLS84);
			list.add(datasetURLS85);
			list.add(datasetURLS86);
			list.add(datasetURLS87);
			list.add(datasetURLS88);
			list.add(datasetURLS89);
			list.add(datasetURLS90);
			list.add(datasetURLS91);
			list.add(datasetURLS92);
			list.add(datasetURLS93);
			list.add(datasetURLS94);
			list.add(datasetURLS95);
			list.add(datasetURLS96);
			list.add(datasetURLS97);
			list.add(datasetURLS98);
			list.add(datasetURLS99);
			list.add(datasetURLS100);
			list.add(datasetURLS101);
			list.add(datasetURLS102);
			list.add(datasetURLS103);
			list.add(datasetURLS104);
			list.add(datasetURLS105);
			list.add(datasetURLS106);
			list.add(datasetURLS107);
			list.add(datasetURLS108);
			list.add(datasetURLS109);
			list.add(datasetURLS110);
			list.add(datasetURLS111);
			list.add(datasetURLS112);
			list.add(datasetURLS113);
			list.add(datasetURLS114);
			list.add(datasetURLS115);
			list.add(datasetURLS116);
			list.add(datasetURLS117);
			list.add(datasetURLS118);
			list.add(datasetURLS119);
			list.add(datasetURLS120);
			list.add(datasetURLS121);
			list.add(datasetURLS122);
			list.add(datasetURLS123);
			list.add(datasetURLS124);
			list.add(datasetURLS125);
			list.add(datasetURLS126);
			list.add(datasetURLS127);
			list.add(datasetURLS128);
			list.add(datasetURLS129);
			list.add(datasetURLS130);
			list.add(datasetURLS131);
			list.add(datasetURLS132);
			list.add(datasetURLS133);
			list.add(datasetURLS134);
			list.add(datasetURLS135);
			list.add(datasetURLS136);
			list.add(datasetURLS137);
			list.add(datasetURLS138);
			list.add(datasetURLS139);
			list.add(datasetURLS140);
			list.add(datasetURLS141);
			list.add(datasetURLS142);
			list.add(datasetURLS143);
			list.add(datasetURLS144);
			list.add(datasetURLS145);
			list.add(datasetURLS146);
			list.add(datasetURLS147);
			list.add(datasetURLS148);
			list.add(datasetURLS149);
			list.add(datasetURLS150);
			list.add(datasetURLS151);
			list.add(datasetURLS152);
			list.add(datasetURLS153);
			list.add(datasetURLS154);
			list.add(datasetURLS155);
			list.add(datasetURLS156);
			list.add(datasetURLS157);
			list.add(datasetURLS158);
			list.add(datasetURLS159);
			list.add(datasetURLS160);
			list.add(datasetURLS161);
			list.add(datasetURLS162);
			list.add(datasetURLS163);
			list.add(datasetURLS164);
			list.add(datasetURLS165);
			list.add(datasetURLS166);
			list.add(datasetURLS167);
			list.add(datasetURLS168);
			list.add(datasetURLS169);
			list.add(datasetURLS170);

		
		set.addAll(list);
	
		}
		return set;
		
		
	
	}

	
	

}
