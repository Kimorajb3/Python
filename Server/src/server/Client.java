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
public class Client extends NetworkConnection {
    
    private int port;
    private String ip;
    
    
    public Client(String ip, int port, Consumer<Serializable> onReceiveCallback){
        super(onReceiveCallback);
        this.ip = ip;
        this.port = port;
        
    }

    @Override
    protected boolean isServer() {
    return false;
    }

    @Override
    protected String getIP() {
        return ip;
    }

    @Override
    protected int getPort() {
        return port;
    }
    
    
}