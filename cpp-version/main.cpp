#include<qapplication.h>
#include<qwidget.h>

int main(int argc, char**argv)
{
    //declare qt main application class with arguments
    QApplication qt_app(argc, argv);

    //create a window widget object
    QWidget *window = new QWidget();

    //declare a size object for size of window
    QSize window_size;
    window_size.setWidth(600);
    window_size.setHeight(400);

    //declare a point object for location of window
    QPoint window_location;
    window_location.setX(100);
    window_location.setY(80);

    //set properties to window
    window->resize(window_size);
    window->move(window_location);
    window->setWindowTitle("Universe");

    //display the window
    window->show();

    //return the executable result
    return qt_app.exec();
}
