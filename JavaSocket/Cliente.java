import java.io.PrintWriter;
import java.net.Socket;

public class Cliente {
	private Socket socketCliente;
	
	public Cliente() throws Exception{
		System.out.println("Fazendo Conex�o");
		socketCliente = new Socket("172.16.3.61", 999);
	}
	
	public void conectarEnviar() throws Exception{
		PrintWriter escritor = new PrintWriter(socketCliente.getOutputStream());
		System.out.println("...");
		escritor.write("...");
		escritor.close();
	}

}
