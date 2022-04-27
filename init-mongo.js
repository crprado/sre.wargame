db.createUser(
    {
     user : "gameapp",
     pwd  : "nonprodthing",
     roles: [
      {
       role : "readWrite",
       db   : "gamehistory"
           }
          ]
    }
  )
  