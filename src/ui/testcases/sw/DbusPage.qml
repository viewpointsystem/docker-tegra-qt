import QtQuick 2.7
import QtQuick.Controls 2.1
import QtQuick.Controls.Material 2.1
import QtQuick.Layouts 1.3
import Dbus 1.0


Pane {
    id: dbus
    anchors.fill: parent
    property string address
    property var self : dbus;

    DbusService {
        id: dbusService
        Component.onCompleted: {
            console.log("Dbus address is: " + dbusService.address);
        }
    }

    ColumnLayout{
        anchors.fill: parent
         
        Item {
            Layout.fillWidth: true
            Layout.fillHeight: true

            Text {
                text: "DBus with gst service test"
                font.family: "Helvetica"
                font.pointSize: 24
                color: "white"
            }
        }

        Item {
            Layout.fillWidth: true
            Layout.preferredHeight:500 
            Layout.maximumHeight:300
            Button {
                id: button
                anchors.centerIn: parent 
                text: "\u2713" // Unicode Character 'CHECK MARK'
                font.pointSize: 50
                width: parent.width 
                height: parent.height
                onClicked: dbusService.play()
            }  
        }
    }
}