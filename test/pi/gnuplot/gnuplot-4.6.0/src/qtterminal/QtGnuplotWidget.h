/* GNUPLOT - QtGnuplotWidget.h */

/*[
 * Copyright 2009   Jérôme Lodewyck
 *
 * Permission to use, copy, and distribute this software and its
 * documentation for any purpose with or without fee is hereby granted,
 * provided that the above copyright notice appear in all copies and
 * that both that copyright notice and this permission notice appear
 * in supporting documentation.
 *
 * Permission to modify the software is granted, but not the right to
 * distribute the complete modified source code.  Modifications are to
 * be distributed as patches to the released version.  Permission to
 * distribute binaries produced by compiling modified sources is granted,
 * provided you
 *   1. distribute the corresponding source modifications from the
 *    released version in the form of a patch file along with the binaries,
 *   2. add special version identification to distinguish your version
 *    in addition to the base release version number,
 *   3. provide your name and address as the primary contact for the
 *    support of your modified version, and
 *   4. retain our contact information in regard to use of the base
 *    software.
 * Permission to distribute the released version of the source code along
 * with corresponding source modifications in the form of a patch file is
 * granted with same provisions 2 through 4 for binary distributions.
 *
 * This software is provided "as is" without express or implied warranty
 * to the extent permitted by applicable law.
 *
 *
 * Alternatively, the contents of this file may be used under the terms of the
 * GNU General Public License Version 2 or later (the "GPL"), in which case the
 * provisions of GPL are applicable instead of those above. If you wish to allow
 * use of your version of this file only under the terms of the GPL and not
 * to allow others to use your version of this file under the above gnuplot
 * license, indicate your decision by deleting the provisions above and replace
 * them with the notice and other provisions required by the GPL. If you do not
 * delete the provisions above, a recipient may use your version of this file
 * under either the GPL or the gnuplot license.
]*/

#ifndef QTGNUPLOTWIDGET_H
#define QTGNUPLOTWIDGET_H

#include "QtGnuplotEvent.h"

#include <QWidget>

class QtGnuplotScene;
class QGraphicsView;
class Ui_settingsDialog;

class QtGnuplotWidget : public QWidget, public QtGnuplotEventReceiver
{
Q_OBJECT

public:
	QtGnuplotWidget(int id = 0, QtGnuplotEventHandler* eventHandler = 0, QWidget* parent = 0);

public:
	bool isActive() const;
	void setStatusText(const QString& status);
	QSize plotAreaSize() const;
	// these can be set from the tool widget or from the command line
	bool m_rounded;
	QColor m_backgroundColor;

signals:
	void statusTextChanged(const QString& status);

public:
	void processEvent(QtGnuplotEventType type, QDataStream& in);

public slots:
	void copyToClipboard();
	void print();
	void exportToPdf();
	void exportToEps();
	void exportToImage();
	void exportToSvg();
	void showSettingsDialog();
	void settingsSelectBackgroundColor();

// Qt functions
protected:
	virtual void resizeEvent(QResizeEvent* event);

private:
	void setViewMatrix();
	QPixmap createPixmap();
	void loadSettings();
	void applySettings();
	void saveSettings();

private:
	int m_id;
	bool m_active;
	QtGnuplotScene* m_scene;
	QGraphicsView* m_view;
	QSize m_lastSizeRequest;

	static int m_widgetUid;

	// Settings
	Ui_settingsDialog* m_ui;
	QColor m_chosenBackgroundColor;
	bool m_antialias;
	bool m_replotOnResize;
};

#endif // QTGNUPLOTWIDGET_H
