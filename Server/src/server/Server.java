/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package server;

import java.io.Serializable;
import java.util.function.Consumer;

/**************************************************************

   Kimora Bailey

   Mini Project - November 14, 2021

 **************************************************************/
public class Server extends NetworkConnection {
    
    private int port;
    
    
    public Server(int port, Consumer<Serializable> onReceiveCallback){
        super(onReceiveCallback);
        this.port = port;
    }

    @Override
    protected boolean isServer() {
    return true;
    }

    @Override
    protected String getIP() {
        return null;
    }

    @Override
    protected int getPort() {
        return port;
    }
     
}
