import unittest
from py5gmeta.kafka import ksqlmeta
from ksqldb.client import KSQLdbClient

def test_amin():
            # TODO: to be fixed with check connector
            # if(not stream_exists('cits_stream')):
            client = KSQLdbClient("https://cloudplatform.francecentral.cloudapp.azure.com/ksql")
            print(client.get_properties())
            print(client.ksql("show topics;"))
            print(client.ksql("show streams;"))
            print(client.ksql("show tables;"))
            print(client.ksql("show connectors;"))

            ksqlmeta.list_streams(client)
            ksqlmeta.create_datatype_connector(client, "cits", "sname", "activemq_url", "username", "password")
            ksqlmeta.create_sink_messages_connector(client,"events_5gmeta", "dest_tp_event", "JMS_SINK_TP1", "tcp://akkodismec.con:61616", "5gmeta-platform", "5gmeta-platform")
            prompt_var = ""
            while prompt_var != "y":
                print(ksqlmeta.list_streams(client))
                print("Before querying check that the topic and the associated schema into the registry exist!")
                prompt_var = input("Continue... ? [y/n]")
            # ATTENTION: when create a stream check that the topic and the associated schema into the registry exist!
            ksqlmeta.create_stream_from_topic(client, "teststream","cits")
            # Then query a topic to filter it
            ksqlmeta.query_stream_to_topic(client, 'ksql-unitest-cits_query001', "teststream")  # 0123012301230123001
            print("Streams list: ")
            print(ksqlmeta.list_streams(client))


if __name__ == '__main__':
    test_amin()