 #include "UDPClient.hpp"

int main()
{
	boost::asio::io_service io_service;
	UDPClient client(io_service, "localhost", "9999");

	client.send("Hello, World!");
}
