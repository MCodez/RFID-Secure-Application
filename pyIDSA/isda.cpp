#include "isda.h"
#include "ui_isda.h"

ISDA::ISDA(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::ISDA)
{
    ui->setupUi(this);
}

ISDA::~ISDA()
{
    delete ui;
}
