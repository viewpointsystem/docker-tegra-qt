import QtQuick 2.11
import QtQuick.Controls 2.4
import QtQuick.Layouts 1.11
import QtQuick.Window 2.2
import QtQuick.Controls.Material 2.4
import Dbus 1.0

import "testcases/sw"
import "layout"

ApplicationWindow {
    id: main_wdw
    objectName: "main_wdw"
    title: "Application Window"
    visible: true

    Material.theme: Material.Dark
    Material.accent: Material.Purple 
    Material.primary: Material.BlueGrey
    
    Page{
        anchors.fill: parent
        
        header: ToolBar {
            RowLayout {
                anchors.fill: parent
                ToolButton {
                    text: qsTr("‹")
                    onClicked: stack.pop()
                }
                Label {
                    text: "Tester"
                    elide: Label.ElideRight
                    horizontalAlignment: Qt.AlignHCenter
                    verticalAlignment: Qt.AlignVCenter
                    Layout.fillWidth: true
                }
                ToolButton {
                    text: qsTr("⋮")
                    onClicked: menu.open()
                }
            }
        }

        DbusPage {}

        footer: ToolBar {
        RowLayout {
            anchors.fill: parent
            ToolButton {
                text: qsTr("‹")
                onClicked: stack.pop()
            }
            Label {
                text: "Astra inclinant, sed non obligant"
                elide: Label.ElideRight
                horizontalAlignment: Qt.AlignHCenter
                verticalAlignment: Qt.AlignVCenter
                Layout.fillWidth: true
            }
            ToolButton {
                text: qsTr("⋮")
                onClicked: menu.open()
            }
        }
        }
    }
} 
    


