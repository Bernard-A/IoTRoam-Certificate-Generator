###  Input Variables 

NetID=000000

make:  certs/network-server/api certs/application-server/api certs/application-server/join-api certs/network-server/roaming

clean:
	rm -rf certs/network-server/api certs/application-server/api certs/application-server/join-api certs/network-server/roaming


# Network Server Certificate Generation 
certs/network-server/api

	# Client Certificate Creation
	
	mkdir -p certs/network-server/api/client
	cfssl gencert -ca certs/intermediate/intermediate.pem -ca-key certs/intermediate/intermediate-key.pem -config config/config.json -profile client config/network-server/api/client/certificate.json | cfssljson -bare certs/network-server/api/client/network-server-api-client
	cat certs/network-server/api/client/network-server-api-client.pem certs/intermediate/intermediate.pem >certs/network-server/api/client/network-server-api-client-combined.pem
   
        # Server Certificate Creation
	
	mkdir -p certs/network-server/api/server
	cfssl gencert -ca certs/intermediate/intermediate.pem -ca-key certs/intermediate/intermediate-key.pem -config config/config.json -profile server config/network-server/api/server/certificate.json | cfssljson -bare certs/network-server/api/server/network-server-api-server
	cat certs/network-server/api/server/network-server-api-server.pem certs/intermediate/intermediate.pem >certs/network-server/api/server/network-server-api-server-combined.pem

# Application Server Certificate Generation
certs/application-server/api

	# Client Certificate Creation
	
	mkdir -p certs/application-server/api/client
	cfssl gencert -ca certs/intermediate/intermediate.pem -ca-key certs/intermediate/intermediate-key.pem -config config/config.json -profile client config/application-server/api/client/certificate.json | cfssljson -bare certs/application-server/api/client/application-server-api-client
	cat certs/application-server/api/client/application-server-api-client.pem certs/intermediate/intermediate.pem >certs/application-server/api/client/application-server-api-client-combined.pem

	# Server Certificate Creation
	mkdir -p certs/application-server/api/server
	cfssl gencert -ca certs/intermediate/intermediate.pem -ca-key certs/intermediate/intermediate-key.pem -config config/config.json -profile server config/application-server/api/server/certificate.json | cfssljson -bare certs/application-server/api/server/application-server-api-server
	cat certs/application-server/api/server/application-server-api-server.pem certs/intermediate/intermediate.pem >certs/application-server/api/server/application-server-api-server-combined.pem

# Join API Certificate Generation
certs/application-server/join-api
	
	# Client Certificate Creation
	
	mkdir -p certs/application-server/join-api/client
	cfssl gencert -ca certs/intermediate/intermediate.pem -ca-key certs/intermediate/intermediate-key.pem -config config/config.json -profile client  config/application-server/join-api/client/certificate.json | cfssljson -bare certs/application-server/join-api/client/application-server-join-api-client 
	cat certs/application-server/join-api/client/application-server-join-api-client.pem certs/intermediate/intermediate.pem >certs/application-server/join-api/client/application-server-join-api-client-combined.pem

        # Server Certificate Creation
	
	mkdir -p certs/application-server/join-api/server
	cfssl gencert -ca certs/intermediate/intermediate.pem -ca-key certs/intermediate/intermediate-key.pem -config config/config.json -profile server  config/application-server/join-api/server/certificate.json | cfssljson -bare certs/application-server/join-api/server/application-server-join-api-server
	cat certs/application-server/join-api/server/application-server-join-api-server.pem certs/intermediate/intermediate.pem >certs/application-server/join-api/server/application-server-join-api-server-combined.pem 

# Roaming Certificate Generation
certs/network-server/roaming

        # Client Certificate Creation
	
	mkdir -p certs/network-server/roaming/${NetID}/client
	cfssl gencert -ca certs/intermediate/intermediate.pem -ca-key certs/intermediate/intermediate-key.pem -config config/config.json -profile client config/network-server/roaming/${NetID}/client/certificate.json | cfssljson -bare certs/network-server/roaming/${NetID}/client/client

	cat certs/network-server/roaming/${NetID}/client/client.pem certs/intermediate/intermediate.pem >certs/network-server/roaming/${NetID}/client/client-combined.pem

	# Server Certificate Creation
	
	mkdir -p certs/network-server/roaming/${NetID}/server
	cfssl gencert -ca certs/intermediate/intermediate.pem -ca-key certs/intermediate/intermediate-key.pem -config config/config.json -profile server config/network-server/roaming/${NetID}/server/certificate.json | cfssljson -bare certs/network-server/roaming/${NetID}/server/server

	cat certs/network-server/roaming/${NetID}/server/server.pem certs/intermediate/intermediate.pem >certs/network-server/roaming/${NetID}/server/server-combined.pem
