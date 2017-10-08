#ifndef ISDA_H
#define ISDA_H

#include <QWidget>

namespace Ui {
class ISDA;
}

class ISDA : public QWidget
{
    Q_OBJECT

public:
    explicit ISDA(QWidget *parent = 0);
    ~ISDA();

private:
    Ui::ISDA *ui;
};

#endif // ISDA_H
