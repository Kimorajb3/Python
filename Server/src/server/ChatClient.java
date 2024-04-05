/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package server;

/**************************************************************

   Kimora Bailey

   Mini Project - November 14, 2021

 **************************************************************/
import javafx.application.Application;
import static javafx.application.Application.launch;
import javafx.application.Platform;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.TextArea;
import javafx.scene.control.TextField;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.GridPane;
import javafx.scene.layout.HBox;
import javafx.stage.Stage;

/**
 *
 * @author bellk
 */
public class ChatClient extends Application {
    Button send = new Button("Send");
    TextField tf;
    TextArea textArea;
    private boolean isServer = false;
    private NetworkConnection connection = isServer ? createServer() : createClient();
    
    private Parent createContent(){
        BorderPane bPan = new BorderPane();
       
        GridPane grid = new GridPane();
        grid.setAlignment(Pos.CENTER);
        grid.setPadding(new Insets(40, 40, 40, 40));
        grid.setHgap(10);
        grid.setVgap(10);
 
       textArea = new TextArea();
       grid.add(textArea, 0, 1);
        
        tf = new TextField();
        tf.setPrefHeight(40);
        grid.add(tf, 0,2); 
        
        HBox hbox = new HBox(send);
        hbox.setAlignment(Pos.BOTTOM_CENTER);
        grid.add(hbox, 0, 3);

        
        bPan.setCenter(grid);
        send.setOnAction(event ->{
            String message = isServer ? "Server: " : "Client: ";
            message += tf.getText();
            tf.clear();
            
            textArea.appendText(message + "\n");
            
            try{
                connection.send(message);
            }
            catch(Exception e){
                textArea.appendText("Failed to send\n");
            }
        });
        textArea.setEditable(false);
       
        bPan.setPrefSize(700, 400);
        return bPan;
      
}
        
    public void start(Stage primaryStage) throws Exception{
        primaryStage.setTitle("Client");
        primaryStage.setScene(new Scene(createContent()));
        primaryStage.show();
        
    }
 
   private Server createServer(){
       return new Server(6363, data ->{
           Platform.runLater(() -> { 
              textArea.appendText(data.toString() + "\n"); 
           });
       });
   }
   
   private Client createClient() {
       return new Client("127.0.0.1", 6363, data -> {
           Platform.runLater(() -> { 
              textArea.appendText(data.toString() + "\n"); 
           });
       });
   }
   @Override
   public void init() throws Exception{
      connection.startConnection();
   }
    @Override
   public void stop() throws Exception{
     connection.closeConnection(); 
   }
   
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        launch(args);
    }

}
